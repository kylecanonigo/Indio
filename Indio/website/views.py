from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def chapters(request):
    return render(request, "website/chapters.html")
