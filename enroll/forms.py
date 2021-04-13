import django
from django.forms import widgets
from .models import  User

class StudentRegistration(django.forms.ModelForm):
    class Meta:
        model=User
        fields = ['name','email','password']
        widgets={
            'name':django.forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email':django.forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'password':django.forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passid'}),
        }