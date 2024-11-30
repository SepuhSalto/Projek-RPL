from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'password', 'Lokasi']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserFormlogin(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
