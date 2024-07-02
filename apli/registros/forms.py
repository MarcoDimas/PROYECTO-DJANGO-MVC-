from django import forms
from .models import ComentarioContacto

class ComentarioContactoForms(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

