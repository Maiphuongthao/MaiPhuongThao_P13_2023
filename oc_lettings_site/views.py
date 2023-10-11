from django.shortcuts import render


def index(request):
    """
    Active front page
    """
    return render(request, "index.html")
