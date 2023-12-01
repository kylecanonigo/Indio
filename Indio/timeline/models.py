from django.db import models

from chapters.models import Lessons


# Create your models here.

class TimelineTypeGame(models.Model):
    game_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='timeline/files/timeline_game')
    image2 = models.ImageField(upload_to='timeline/files/timeline_game')
    image3 = models.ImageField(upload_to='timeline/files/timeline_game')
    correct_img1 = models.ImageField(upload_to='timeline/files/timeline_game')
    correct_img2 = models.ImageField(upload_to='timeline/files/timeline_game')
    correct_img3 = models.ImageField(upload_to='timeline/files/timeline_game')

    def __str__(self):
        return f"Game ID: {self.game_id}, Lesson: {self.lesson}"
