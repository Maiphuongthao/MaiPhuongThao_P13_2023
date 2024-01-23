from django.shortcuts import render
import sentry_sdk


def index(request):
    """
    Active front page
    """
    return render(request, "index.html")


def trigger_error(request):
    """
    Active division zero to test Sentry exception err capture.
    put http request and get the response
    """
    try:
        return 1/0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
