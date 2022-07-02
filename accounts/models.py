import imp
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="featured_images/", default="featured_images/featured.jpg")
    secret_code = models.CharField(max_length=20, blank=True, null=True, help_text="added to email to verify sender and limit spam")
    
    def __str__(self):
        return f"{self.user.username} - profile"