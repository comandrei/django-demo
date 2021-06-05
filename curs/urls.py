from django.urls import path
from .views import hello, show_students, show_student, show_curs, contact

urlpatterns = [
    path('', hello),
    path('students/', show_students, name="student_list"),
    path('student/<int:student_id>/', show_student, name="student_detail"),
    path('curs/<int:curs_id>/', show_curs, name="curs_detail"),
    path('contact', contact),
] 