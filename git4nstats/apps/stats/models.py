from django.db import models


class BaseModel(models.Model):
    """
    Abstract class to help models.
    """
    created_at = models.DateTimeField(
        verbose_name='created at'
    )

    class Meta:
        abstract = True


class GitHubUser(BaseModel):
    login = models.CharField(
        max_length=250,
        verbose_name='login'
    )
    github_id = models.IntegerField(
        verbose_name='github_id'
    )
    name = models.CharField(
        verbose_name='name',
        max_length=250,
        null=True,
        default=''
    )
    data = models.JSONField()


class Gist(BaseModel):
    gist_id = models.CharField(
        verbose_name='gist_id',
        max_length=250
    )
    description = models.TextField()
    data = models.JSONField()
    github_user = models.ForeignKey(
        GitHubUser,
        related_name='gist',
        on_delete=models.CASCADE
    )


class Event(BaseModel):
    event_id = models.CharField(
        verbose_name='event_id',
        max_length=250,
    )
    github_type = models.CharField(
        verbose_name='github_type',
        max_length=250,
    )
    data = models.JSONField()
    github_user = models.ForeignKey(
        GitHubUser,
        related_name='events',
        on_delete=models.CASCADE
    )
