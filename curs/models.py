from django.db import models

# Create your models here.

class Student(models.Model):
    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20)
