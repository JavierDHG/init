from dataclasses import field
from pyexpat import model
from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields ='__all__'

