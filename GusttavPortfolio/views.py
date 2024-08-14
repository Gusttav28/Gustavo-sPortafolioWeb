# the django http and the httpresponse are create a reponse from the server to the user
from django.http import HttpResponse

# here from shorcuts we are importing render to see the html file
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about_me(request):
    return render(request, "about_me.html")

def resume(request):
    return render(request, "resume.html")

def contac(request):
    return render(request, "contac.html")
