from django import forms

from .models import Student

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(max_length=100, widget=forms.Textarea)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)