from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Show list of profiles
    :param request from user
    :return a list of profile
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Show a profile
    :params request and username
    :return a profile from username
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
