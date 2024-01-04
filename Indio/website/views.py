from django.shortcuts import render
from django.views import View


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, "website/index.html")


class AboutView(View):
    def get(self, request):
        return render(request, "website/about.html")
