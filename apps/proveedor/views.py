from django.shortcuts import render
from django.views.generic  import View, CreateView, ListView, UpdateView, DeleteView

from .models import *
from .forms import *

# Create your views here.

class IngresarProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    succes_url = '//'

class Proveedores(ListView):
    model = Proveedor
    queryset = Proveedor.objects.all()
    template_name = 'proveedor/proveedor_list.html'
    context_object_name = 'proveedores'

class IngresarCuenta(CreateView):
    model = CuentasProveedor
    succes_url = '//'
    fields = ('proveedor', 'banco', 'tipo_cuenta', 'numero_cuenta')

class Cuentas(CreateView):
    model = CuentasProveedor
    queryset = CuentasProveedor.objects.all().order_by('proveedor')
    template_name = 'proveedor/cuentas_list.html'
    context_object_name = 'cuentas'
