from django.shortcuts import render

# Create your views here.


def four(request):
    return render(request, "four/four.html")
