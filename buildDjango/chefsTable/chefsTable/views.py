from django.http import HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound('Page Not Found')