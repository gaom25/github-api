from typing import Any, Dict, List

from concurrent.futures import ThreadPoolExecutor
import threading

from github.connector import GitHubConnector
from stats.models import (
    GitHubUser,
    Gist,
    Event
)
from stats import selectors as stats_sel
from stats.constants import (
    MAX_EVENTS,
    MAX_GISTS,
    MAX_WORKERS
)

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = GitHubConnector()
    return thread_local.session


def find_github_users(github_users: List[str]) -> List[Dict[str, Any]]:
    res = []
    for github_user in github_users:
        result = create_gh_user_gists_events(github_user)
        res.append(result)

    return res


def create_gh_user_gists_events(github_user: str) -> Dict[str, Any]:
    gh_user_qs = stats_sel.filter_gh_user_by_user_id(user_id=github_user)
    if not bool(gh_user_qs):
        gh_user = create_github_user(github_user=github_user)
    else:
        gh_user = gh_user_qs.first()
    executors_list = []
    result = {
        'user': gh_user.login
    }
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executors_list.append(executor.submit(find_gists, gh_user))
        executors_list.append(executor.submit(find_events, gh_user))

    for x in executors_list:
        res = x.result()
        res_type = res.get('type')
        res_data = res.get('data')
        if res_type == 'gist':
            result.update(gists=res_data)
            continue
        if res_type == 'event':
            result.update(events=res_data)

    return result


def create_github_user(github_user: str) -> GitHubUser:
    github_connector = GitHubConnector()
    response_user = github_connector.user.get(user_id=github_user)
    return create_user(response_data=response_user)


def create_user(response_data: Dict[str, Any]) -> GitHubUser:
    login = response_data.get('login')
    github_id = response_data.get('id')
    name = response_data.get('name')
    created_at = response_data.get('created_at')
    return GitHubUser.objects.create(
        created_at=created_at,
        login=login,
        github_id=github_id,
        name=name,
        data=response_data
    )


def find_gists(github_user: GitHubUser) -> Dict[str, Any]:
    github_connector = get_session()
    gh_user_id = github_user.login
    response_gists = github_connector.gists.get(user_id=gh_user_id)
    gist_count = 0
    result = {
        'type': 'gist'
    }
    data = []
    gist_len = len(response_gists)
    while gist_count < MAX_GISTS and gist_count < gist_len:
        gist_data = response_gists[gist_count]
        create_gists(response_data=gist_data, user=github_user)
        gist_count += 1
        data.append(gist_data)
    result.update(data=data)
    return result


def create_gists(response_data: Dict[str, Any], user: GitHubUser) -> Gist:
    gist_id = response_data.get('id')
    description = response_data.get('description')
    created_at = response_data.get('created_at')
    return Gist.objects.create(
        created_at=created_at,
        gist_id=gist_id,
        description=description,
        data=response_data,
        github_user=user
    )


def find_events(github_user: GitHubUser) -> Dict[str, Any]:
    github_connector = get_session()
    gh_user_id = github_user.login
    response_events = github_connector.events.get(user_id=gh_user_id)
    events_count = 0
    result = {
        'type': 'event'
    }
    data = {}
    events_len = len(response_events)
    while events_count < MAX_EVENTS and events_count < events_len:
        events_data = response_events[events_count]
        event = create_events(response_data=events_data, user=github_user)
        events_count += 1
        data[event.event_id] = events_data
    result.update(data=data)
    return result


def create_events(response_data: Dict[str, Any], user: GitHubUser) -> Event:
    event_id = response_data.get('id')
    github_type = response_data.get('type')
    created_at = response_data.get('created_at')
    return Event.objects.create(
        created_at=created_at,
        event_id=event_id,
        github_type=github_type,
        data=response_data,
        github_user=user
    )
