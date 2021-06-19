from django.urls import path
from .views import hello, show_students, show_student, show_curs,\
     contact, add_student, edit_student, login_view, logout_view, api_student 

urlpatterns = [
    path('', hello),
    path('students/', show_students, name="student_list"),
    path('student/<int:student_id>/', show_student, name="student_detail"),
    path('curs/<int:curs_id>/', show_curs, name="curs_detail"),
    path('contact', contact),
    path('add_student', add_student),
    path('edit_student/<int:student_id>/', edit_student),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),

    path('api/student/<int:student_id>', api_student),

] 