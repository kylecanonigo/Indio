from django.contrib import admin

from chapters.models import Chapters, Lessons, LessonMaterials

# Register your models here.


admin.site.register(Chapters)
admin.site.register(Lessons)
admin.site.register(LessonMaterials)

