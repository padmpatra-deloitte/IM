from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='projects', default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Issue(models.Model):
    # TYPE_BUG = 'B'
    # TYPE_TASK = 'T'
    # TYPE_STORY = 'S'
    # TYPE_EPIC = 'E'
    # TYPE_CHOICES = [
    #     (TYPE_BUG, 'Bug'),
    #     (TYPE_TASK, 'Task'),
    #     (TYPE_STORY, 'Story'),
    #     (TYPE_EPIC, 'Epic')
    # ]

    title = models.CharField(max_length=150)
    desc = models.TextField()
    belong_to = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues")
    reporter = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='reporter', default=None)
    assignee = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='assignee', null=True)
    type = models.ForeignKey(
        'tag.Tag', related_name='tagged_issues', on_delete=models.PROTECT, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
