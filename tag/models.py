from django.db import models

# Create your models here.


class Tag(models.Model):
    title=models.CharField(max_length=10, null=False, blank=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)