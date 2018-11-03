from django import forms


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Busqueda')

class ContactoForm(forms.Form):
    contact_nombre = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

