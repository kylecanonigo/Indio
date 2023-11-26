from django.db import models

# Create your models here.


class Chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_number = models.IntegerField()


class Lessons(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lesson_number = models.IntegerField()
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)


class LessonMaterials(models.Model):
    material_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    material_text = models.TextField()
    image1 = models.ImageField(upload_to='lesson_materials')
    image2 = models.ImageField(upload_to='lesson_materials')
    image3 = models.ImageField(upload_to='lesson_materials')

