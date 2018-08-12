from .models import *
from django import forms

class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Nombre proveedor',
                'required': True}),
        label='Nombre:')

    apellido = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Apellido proveedor',
                'required': True}),
        label='Apellido:')

    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Direccion proveedor',
                'required': True}),
        label='Direccion:')

    cedula = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Cedula proveedor',
                'required': True}),
        label='Cedula:')

    telefono = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Telefono proveedor',
                'required': True, 'minlength':9,
                'maxlength':10}),
        label='Telefono:')

    correo = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Correo proveedor',
                'required': True}),
        label='Correo:')

    ruc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'RUC proveedor',
                'required': True}),
        label='RUC:')

    class Meta:
        model = Proveedor
        fields = ('nombre', 'apellido','cedula',
                'direccion', 'cedula', 'telefono',
                 'correo', 'ruc')
