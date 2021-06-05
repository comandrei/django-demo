from django import forms

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(max_length=100, widget=forms.Textarea)

class StudentForm(forms.Form):
    nume = forms.CharField(max_length=20)
    prenume = forms.CharField(max_length=20)
    an = forms.IntegerField()