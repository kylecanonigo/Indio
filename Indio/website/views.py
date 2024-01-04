from django.shortcuts import render
from django.views import View


# Create your views here.


class Index(View):
        def get(self, request):
            request.session['word_index'] = 0
            return render(request, "website/index.html")

class About(View):
    def get(self, request):
        return render(request, "website/about.html")

