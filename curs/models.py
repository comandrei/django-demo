from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curs(models.Model):
    nume = models.CharField(max_length=20)

    def __str__(self):
        return self.nume


class StudentManager(models.Manager):

    def seniors(self):
        return self.filter(an=4)


class Student(models.Model):
    class Meta:
        ordering = ("nume", )
        unique_together = ("nume", "prenume")

    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20, db_index=True)
    cursuri = models.ManyToManyField(Curs)
    an = models.IntegerField(default=1)
    
    objects = StudentManager()

    def __str__(self):
        course_count = self.cursuri.count()
        if course_count:
            return f'{self.prenume} {self.nume} {course_count}'
        else:
            return f'{self.prenume} {self.nume}'
    
    def metoda_mea(self):
        pass

 

class Note(models.Model):
    nota = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.student} {self.nota}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cod_postal = models.CharField(max_length=20)
