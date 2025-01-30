from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Formulario de Registro de Usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditarPerfilForm(forms.ModelForm):
    password = None 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']