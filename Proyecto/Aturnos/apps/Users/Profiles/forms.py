from django import forms
from .models import Users
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Users
        fields ='__all__'