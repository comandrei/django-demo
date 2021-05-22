from django.urls import path
from .views import hello, show_students

urlpatterns = [
    path('', hello),
    path('students/', show_students)
] 