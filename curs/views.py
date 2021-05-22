from django.shortcuts import render

from django.db.models import Q
from .models import Student

def hello(request):
    return render(request, "index.html", {'name': 'dorel'})

def show_students(request):
    if 'search' in request.GET:
        search = request.GET['search']
        lista_studenti = Student.objects.filter(Q(nume__iexact=search) | Q(prenume__iexact=search))
        print(str(lista_studenti.query))
    else:
        lista_studenti = Student.objects.all()
    return render(request, "show_students.html", {"students": lista_studenti})