from django.shortcuts import render, get_object_or_404

from django.db.models import Q
from .models import Student, Curs

def hello(request):
    my_dict = {
        'unu': 1,
        'doi': 2
    }
    my_list = [1,2,3]
    return render(request, "index.html", {'name': 'dorel', 'my_dict': my_dict, 'my_list': my_list })

def show_students(request):
    if 'search' in request.GET:
        search = request.GET['search']
        lista_studenti = Student.objects.filter(Q(nume__iexact=search) | Q(prenume__iexact=search))
        print(str(lista_studenti.query))
    else:
        lista_studenti = Student.objects.prefetch_related('cursuri').all()
    return render(request, "show_students.html", {"students": lista_studenti})

def show_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    # try:
    #     student = Student.objects.get(pk=student_id)
    #     render()
    # except Student.DoesNotExist:
    #     return 404
    return render(request, "show_student.html", {"student": student})

def show_curs(request, curs_id):
    curs = get_object_or_404(Curs, id=curs_id)
    return render(request, "show_curs.html", {"curs": curs})