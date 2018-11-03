from django import forms
from django.forms import TextInput

from orders.models import Orden


class OrdenCreateForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['telefono', 'domicilio', 'cp']
        widgets = {
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'domicilio': TextInput(attrs={'class': 'form-control'}),
            'cp': TextInput(attrs={'class': 'form-control'}),
        }