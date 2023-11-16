from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def login(request):
    return render(request, "website/login.html")


def register(request):
    return render(request, "website/register.html")
