"""
here to create models for app_db
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    user=1 to many relation django auth user FK
    favorite_city =str
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
