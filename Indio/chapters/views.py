from django.shortcuts import render
from django.views import View


class ChaptersListView(View):
    def get(self, request):
        return render(request, "chapters/chapters_list.html")


class LessonsListView(View):
    def get(self, request):
        return render(request, "chapters/lessons_list.html")


class DetailView(View):
    def get(self, request, id):
        return render(request, "chapters/detail.html")




