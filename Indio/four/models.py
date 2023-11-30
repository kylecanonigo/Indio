from django.db import models

from chapters.models import Lessons


# Create your models here.

class FourPicsOneWord(models.Model):
    game_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='four/files/four_pics_game')
    image2 = models.ImageField(upload_to='four/files/four_pics_game')
    image3 = models.ImageField(upload_to='four/files/four_pics_game')
    image4 = models.ImageField(upload_to='four/files/four_pics_game')
    correct_answer = models.CharField(max_length=255)

