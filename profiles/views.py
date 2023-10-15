from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
    Show list of profiles
    :param request from user
    :return a list of profile
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Show a profile
    :params request and username
    :return a profile from username
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
