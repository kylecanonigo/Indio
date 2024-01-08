from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from chapters.models import Chapter
from four.models import GameWords


# Create your views here.
class Home(View):

    template = 'website/home.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        if request.method == 'POST':
            try:
                self.reset()
                return JsonResponse({'message': 'Reset successfully'}, status=200)
            except GameWords.DoesNotExist:
                return JsonResponse({'message': 'Record not found'}, status=404)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)

    def reset(self):
        GameWords.objects.all().update(is_ans=False)
        Chapter.objects.all().update(chapter_answered=0)


class Index(View):
    template_name = "website/index.html"

    def get(self, request):
        request.session['word_index'] = 0
        chap1 = self.check(1)
        #print("Chapter 1 status:" + str(chap1))
        chap2 = self.check(2)
        #print("Chapter 2 status:" + str(chap2))
        chap3 = self.check(3)
        #print("Chapter 3 status:" + str(chap3))
        chap4 = self.check(4)
        #print("Chapter 4 status:" + str(chap4))

        self.reset()

        context = {
            'chap1': chap1,
            'chap2': chap2,
            'chap3': chap3,
            'chap4': chap4,
        }
        return render(request, self.template_name, context)


    def check(self, id):
        chapter_num = Chapter.objects.get(chapter_id = id)
        status = chapter_num.chapter_status
        return True if status == "locked" else False




class About(View):
    def get(self, request):
        return render(request, "website/about.html")

