from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request,name):
    #capitalize(): convierte de a letra Mayuscula la inicial
    return HttpResponse(f"Hello, {name.capitalize()}")