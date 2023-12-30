from django.db import models


class Chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"Chapter {self.chapter_number}"


class Lessons(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lesson_number = models.IntegerField()
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lesson {self.lesson_number} (Chapter {self.chapter.chapter_number})"
