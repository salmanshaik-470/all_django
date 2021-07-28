from django.db import models


class Management_Employee(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    pwd = models.CharField(max_length=100)
    emp_id = models.IntegerField(null=True)