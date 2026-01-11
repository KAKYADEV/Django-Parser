from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Hello wanna parse some info?")
