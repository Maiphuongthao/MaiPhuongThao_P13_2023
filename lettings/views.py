from django.shortcuts import render, get_object_or_404
from .models import Letting
import sentry_sdk


def index(request):
    """
    Show list of lettings
    :param request from user
    :return list of letting
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Show a letting
    :params request and letting_id
    :return letting details
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, "error.html", {"error_message": str(e)}, status=500)
