from calendar import monthcalendar
from dataclasses import field
from pyexpat import model
from django import forms
from .models import Usuarios,Turnos

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields ='__all__'

class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'