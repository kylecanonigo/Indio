from django.db import models

from chapters.models import Chapter


# Create your models here.

class GameWords(models.Model):
    word_id = models.AutoField(primary_key=True)
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    word_desc = models.TextField()
    is_ans = models.BooleanField()

    def __str__(self):
        return f"Word ID: {self.word_id}, Chapter: {self.chapter_id}, Correct Answer: {self.word}"
