import imp
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    my_signature = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"