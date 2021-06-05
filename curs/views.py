from django.shortcuts import redirect, render, get_object_or_404

from django.db.models import Q
from django.core.mail import send_mail
from .forms import ContactForm, StudentForm
from .models import Student, Curs

def my_func():
    return 'func'

def hello(request):
    my_dict = {
        'unu': 1,
        'doi': 2
    }
    my_list = [1,2,3]
    ctx = { 
        'name': 'dorel',
        'my_dict': my_dict,
        'my_list': my_list,
        'my_func': my_func 
    }
    if True:
        del ctx['my_dict']
    return render(request, "index.html", ctx)

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

def add_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
    else:
        student_form = StudentForm(initial = {"nume": "Dorel"})
    return render(request, "add_student.html", {"form": student_form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    saved = False
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            saved = True
        
    else:
        student_form = StudentForm(instance=student)
    return render(request, "add_student.html", {"form": student_form, "saved": saved})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            send_mail('subject',
                form.cleaned_data['message'],
                [form.cleaned_data['email']],
                ['contact@domeniu.com'])
        else:
            form_data = {}
    else:
        form = ContactForm()
        form_data = {}
    return render(request, "contact.html", {'form': form, 'form_data': form_data})