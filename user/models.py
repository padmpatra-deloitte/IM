from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone_no = models.CharField(max_length=15)
    profile_picture = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.username or not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email