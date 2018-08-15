from django import forms
from apps.local.models import Local, StockLocal

from .models import *
#Multiples formularios
from django.forms.models import inlineformset_factory,\
    formset_factory

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
        queryset=StockLocal.objects.all(),
        widget=forms.Select(
            attrs={'list':'productos'}),
        empty_label='Productos')

    cantidad = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'cantidad-producto',
               'placeholder':'Catidad de productos'}))

    precio = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class':'precio-producto', 'step':'any',
               'placeholder':'Precio'}),
        max_digits=5, decimal_places=2)

    total = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class':'total-producto', 'step':'any',
               'placeholder':'Total'}),
        max_digits=5, decimal_places=2)

    class Meta:
        model=DetalleVenta
        fields=('producto','cantidad','precio','total')

DetalleVentaFormSet = inlineformset_factory(
                      Venta,DetalleVenta,
                      extra=5,form=DetalleVentaForm)
