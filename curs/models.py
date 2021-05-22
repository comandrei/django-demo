from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        ordering = ("nume", )
    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.prenume} {self.nume}'
