from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to Homepage. \n  Go to /Details for more information ")