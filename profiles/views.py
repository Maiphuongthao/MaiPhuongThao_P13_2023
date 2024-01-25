from django.shortcuts import render, get_object_or_404
from .models import Profile
import sentry_sdk


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
    capture err to sentry if there is
    """
    try: 
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "error.html", {"error_message":str(e)}, status=500)
