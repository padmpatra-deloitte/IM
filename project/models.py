from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


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
    belong_to = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="issues")
    # type  = models.CharField(max_length=1, choices=TYPE_CHOICES, default=TYPE_BUG)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
