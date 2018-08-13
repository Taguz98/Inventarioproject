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
        label='Seleciones un categoria:')

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
        fields = ('proveedor', 'local')

class DetalleIngresoForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(),
        empty_label='Productos',
        label='Seleciones un producto:')

    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
        attrs={'placeholder':'Cantidad producto'}),
        label='Cantidad:')

    precio_compra = forms.DecimalField(
        max_digits = 5, decimal_places = 2,
        label='Precio Compra:')

    precio_venta = forms.DecimalField(
        max_digits = 5, decimal_places = 2,
        label='Precio Venta:')

    precio_descuento = forms.DecimalField(
        max_digits = 5, decimal_places = 2,
        label='Precio Descuento:')

    class Meta:
        model = DetalleIngreso
        fields = ('producto', 'cantidad', 'precio_compra',
                  'precio_venta', 'precio_descuento')

#Ingreso multiple
DetalleIngresoFormSet = inlineformset_factory(
                        Ingreso, DetalleIngreso,
                        extra=5, form=DetalleIngresoForm)

class EnvioForm(forms.ModelForm):
    local_salida = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'minlength':3,
                'maxlength':50}),
        label='Local salida:', initial='Local Principal')

    local_llegada = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        widget=forms.Select(),
        empty_label='Locales',
        label='Local llegada:')

    descripcion = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Descripcion Envio',
                'minlength':5,'maxlength':200,
                'size':70}),
        label='Descripcion:')

    class Meta:
        model = Envio
        fields = ('local_salida','local_llegada',
                  'descripcion')

class DetalleEnvioForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(),
        empty_label='Productos',
        label='Selecione un producto:')

    cantidad = forms.IntegerField(
        widget=forms.NumberInput(
        attrs={'placeholder':'Cantidad producto'}),
        label='Cantidad:')

    class Meta:
        model = DetalleEnvio
        fields = ('producto', 'cantidad')

DetalleEnvioFormSet = inlineformset_factory(
                      Envio, DetalleEnvio,
                      extra=4, form=DetalleEnvioForm)

class VentaForm(forms.ModelForm):
    local = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        widget=forms.Select(),
        empty_label='Locales',
        label='Selecione un local:')
        #initial=Local.objects.get(pk=1)

    cedula = forms.CharField(widget=forms.TextInput(
        attrs={'maxlength':10,'minlength':10}),
        label='Cedula:', initial='9999999999')

    total = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class':'total-venta', 'step':'any'}),
        label='Total:', max_digits=5, decimal_places=2)

    class Meta:
        model = Venta
        fields=('local','cedula','total')

class DetalleVentaForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(),
        empty_label='Productos',
        label='Selecione un producto:')

    cantidad = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'cantidad-producto',
               'placeholder':'Catidad de productos'}),
        label='Cantidad:')

    precio = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class':'precio-producto', 'step':'any'}),
        label='Precio:', max_digits=5, decimal_places=2)

    total = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class':'total-producto', 'step':'any'}),
        label='Total:', max_digits=5, decimal_places=2)

    class Meta:
        model=DetalleVenta
        fields=('producto','cantidad','precio','total')

DetalleVentaFormSet = inlineformset_factory(
                      Venta,DetalleVenta,
                      extra=5,form=DetalleVentaForm)
