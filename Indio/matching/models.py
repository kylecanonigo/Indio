from django.db import models

from chapters.models import Lessons


# Create your models here.

class MatchingTypeGame(models.Model):
    game_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='matching_game')
    image2 = models.ImageField(upload_to='matching_game')
    image3 = models.ImageField(upload_to='matching_game')
    correct_img1 = models.ImageField(upload_to='matching_game')
    correct_img2 = models.ImageField(upload_to='matching_game')

