from django.shortcuts import render

# Create your views here.


def matching(request):
    return render(request, "matching/matching.html")

