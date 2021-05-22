from django.urls import path
from .views import hello, show_students, show_student

urlpatterns = [
    path('', hello),
    path('students/', show_students),
    path('student/<int:student_id>/', show_student)
] 