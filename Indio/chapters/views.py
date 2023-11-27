from django.shortcuts import render

# Create your views here.


def chapters_list(request):
    return render(request, "chapters/chapters_list.html")


def lessons_list(request):
    return render(request, "chapters/lessons_list.html")


def detail(request, id):
    return render(request, "chapters/detail.html")


def congratulations(request):
    return render(request, "chapters/congratulations.html")


