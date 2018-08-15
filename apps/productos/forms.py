from django import forms
from apps.proveedor.models import Proveedor

from apps.local.models import Local

from .models import *
#Multiples formularios
from django.forms.models import inlineformset_factory,\
formset_factory

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Nombre producto',
                'required': True, 'minlength':3,
                'maxlength':50}),
        label='Nombre:')

    descripcion = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Descripcion producto',
                'required': True, 'minlength':5,
                'maxlength':200}),
        label='Descripcion:')

    stock_minimo = forms.IntegerField(
        widget=forms.NumberInput(
        attrs={'placeholder':'Stock minimo'}),
        label='Cantidad:')

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(),
        empty_label='Categorias',
        label='Selecione una categoria:')

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion',
                  'stock_minimo', 'categoria')

class IngresoForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select(),
        empty_label='Proveedores',
        label='Selecione un proveedor:')

    local = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        widget=forms.Select(),
        empty_label='Locales',
        label='Seleciones un local:')

    descripcion = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Descripcion ingreso',
                'minlength':5,'maxlength':200,
                'size':70}),
        label='Descripcion:')

#Size es para hacer el input mas grande
    class Meta:
        model = Ingreso
        fields = ('proveedor', 'local', 'descripcion')

class DetalleIngresoForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(),
        empty_label='Productos',
        label='Selecione un producto:')

    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder':'Cantidad producto'}),
        label='Cantidad:')

    precio_compra = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'placeholder':'Precio compra',
                   'step':'any'}),
        max_digits = 5, decimal_places = 2)

    precio_venta = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'placeholder':'Precio venta',
                   'step':'any'}),
        max_digits = 5, decimal_places = 2)

    precio_descuento = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'placeholder':'Precio descuento',
                   'step':'any'}),
        max_digits = 5, decimal_places = 2)

    class Meta:
        model = DetalleIngreso
        fields = ('producto', 'cantidad','precio_compra',
                  'precio_venta', 'precio_descuento')

#Ingreso multiple
DetalleIngresoFormSet = inlineformset_factory(
                        Ingreso, DetalleIngreso,
                        extra=8, form=DetalleIngresoForm)
