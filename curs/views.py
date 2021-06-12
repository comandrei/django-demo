from django.shortcuts import redirect, render, get_object_or_404

from django.db.models import Q
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, StudentForm, LoginForm
from .models import Student, Curs
from .decorators import view_counter, decorator1

from django.utils import timezone

def my_func():
    return 'func'

@view_counter
@decorator1
def hello(request):
    request.session['today'] = str(timezone.now())
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
    request.session['view_count'] = request.session.get('view_count', 0) + 1
    key = f'cache_{student_id}'
    student = cache.get(key, None)
    if student is None:
        print("miss", key)
        #student = get_object_or_404(Student, pk=student_id)
        student = Student.objects.prefetch_related('cursuri').get(pk=student_id)
        cache.set(key, student, 15)    
    # try:
    #     student = Student.objects.get(pk=student_id)
    #     render()
    # except Student.DoesNotExist:
    #     return 404
    return render(request, "show_student.html", {"student": student})

@cache_page(60)
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


def login_view(request):
    error_message = None
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, "User logat cu success")
                return redirect('/curs')
            else:
                messages.error(request, "Nu avem acest user")
    form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/curs')