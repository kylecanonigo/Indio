from django.db import models

from chapters.models import Lessons


# Create your models here.

class FourPicsOneWord(models.Model):
    game_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Game ID: {self.game_id}, Lesson: {self.lesson}, Correct Answer: {self.correct_answer}"
