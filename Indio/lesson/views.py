from django.shortcuts import render

# Create your views here.


def lesson(request):
    return render(request, "lesson/lesson.html")

