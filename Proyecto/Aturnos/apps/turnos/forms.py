from calendar import monthcalendar
from dataclasses import field
from pyexpat import model
from django import forms
from .models import Turns

class TurnsForm(forms.ModelForm):
    class Meta:
        model = Turns
        fields = '__all__'