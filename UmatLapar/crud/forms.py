from django import forms
from .models import Users, Rating, kategori, Location

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'alamat']
        widgets = {
            'password': forms.PasswordInput(),
            'alamat': forms.TextInput(attrs={'size': '20'}),  # Reduced size to make it smaller horizontally
        }

class UserFormlogin(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserFormupdate(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'hobi', 'pekerjaan', 'alamat', 'foto_profil', 'foto_background']

class UserFormupdatepassword(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RatingCreateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'komentar', 'foto', 'video']


