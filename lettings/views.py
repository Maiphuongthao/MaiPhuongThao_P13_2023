from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    """
    Show list of lettings
    :param request from user
    :return list of letting
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """
    Show a letting
    :params request and letting_id
    :return letting details
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)
