from django.db.models import QuerySet

from stats.models import (
    GitHubUser,
    Gist,
    Event
)


def filter_gh_user_by_user_id(user_id: str) -> 'QuerySet':
    return GitHubUser.objects.filter(login=user_id)
