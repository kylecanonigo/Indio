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

class LessonMaterials(models.Model):
    material_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    material_text = models.TextField()
    image1 = models.ImageField(upload_to='lesson_materials')
    image2 = models.ImageField(upload_to='lesson_materials')
    image3 = models.ImageField(upload_to='lesson_materials')

    def __str__(self):
        return f"Material for Lesson {self.lesson.lesson_number}"
