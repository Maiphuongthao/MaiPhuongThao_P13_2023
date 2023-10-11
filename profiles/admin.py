"""
register add for profile app
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
