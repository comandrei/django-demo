from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curs(models.Model):
    nume = models.CharField(max_length=20)

class Student(models.Model):
    class Meta:
        ordering = ("nume", )
    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20, db_index=True)
    cursuri = models.ManyToManyField(Curs)
    
    def __str__(self):
        return f'{self.prenume} {self.nume}'



class Note(models.Model):
    nota = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.student} {self.nota}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cod_postal = models.CharField(max_length=20)
