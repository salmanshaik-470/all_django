from django.db import models

# Create your models here.
class student(models.Model):
    stdid=models.IntegerField()
    stdname=models.CharField(max_length=70)
