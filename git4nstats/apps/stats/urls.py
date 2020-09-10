from django.urls import path

from stats.views import (
    GitHubUsers
)


urlpatterns = [
    path(
        'github-users/',
        GitHubUsers.as_view()
    ),
]
