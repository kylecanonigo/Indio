from django.db import models

# Create your models here.
class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_title = models.CharField(max_length=100)
    chapter_answered = models.IntegerField()
    chapter_total = models.IntegerField()
    chapter_status = models.CharField(max_length=100, null=False)

    def __str__(self):
        return "Chapter " + self.chapter_id.__str__() + ": " + self.chapter_title.__str__()