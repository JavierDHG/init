from django import forms
from .models import Users
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Users
        fields ='__all__'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget_attrs['class'] = 'form-control'
        self.fields['username'].widget_attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget_attrs['class'] = 'form-control'
        self.fields['password'].widget_attrs['placeholder'] = 'Contraseña'


