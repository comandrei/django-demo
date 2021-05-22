from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

def hello(request):
    return render(request, "index.html", {'name': 'dorel'})

def show_students(request):
    lista_studenti = Student.objects.all()
    return render(request, "show_students.html", {"students": lista_studenti})