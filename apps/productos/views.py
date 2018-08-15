from django.shortcuts import render
from django.views.generic import View, CreateView,\
    ListView, UpdateView, DetailView, DeleteView

from django.shortcuts import render, redirect,\
    render_to_response, HttpResponse, HttpResponseRedirect
#Para hacer una codigo de producto dinamico
from django.contrib.auth.models import User

#Import para actuaalizar el stock dinamico
from apps.local.models import StockLocal

from .models import *
from .forms import *

# Create your views here.

class IngresarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    success_url = '/productos/categorias/'

class Categorias(ListView):
    model = Categoria
    queryset = Categoria.objects.all()
    template_name = 'productos/categoria_list.html'
    context_object_name = 'categorias'

class StockLista(ListView):
    model = Stock
    queryset = Stock.objects.all()
    template_name = 'productos/stock_list.html'
    context_object_name = 'stocks'
    pass

class IngresarProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = '/productos/'

class Productos(ListView):
    model = Producto
    queryset = Producto.objects.all()
    template_name = 'productos/productos_list.html'
    context_object_name = 'productos'

class IngresarIngreso(CreateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'productos/ingreso_form.html'
    success_url = '/productos/ingresos/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DetalleIngresoFormSet()
        return self.render_to_response(
            self.get_context_data(
                form = form,
                formset = DetalleIngresoFormSet))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DetalleIngresoFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        #Aqui deberia ir una funcio que me actualice
        #mi inventario
        ActualizarStock(self.object.id)
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, formset):
        return render_to_response(
            self.get_context_data(
                form = form,
                formset = DetalleIngresoFormSet))

class Ingresos(ListView):
    model = Ingreso
    queryset = Ingreso.objects.all()
    template_name = 'productos/ingresos_list.html'
    context_object_name = 'ingresos'

class DetallesIngreso(ListView):
    model = DetalleIngreso
    queryset = DetalleIngreso.objects.all()
    template_name = 'productos/detallesIngreso_list.html'
    context_object_name = 'detalles'


#Funciones para actualizar el stock

#Al ingresar productos se usa este
def ActualizarStock(id_ingreso):
    #Para pruebas
    for p in DetalleIngreso.objects.filter(id_ingreso=id_ingreso):
        productos = DetalleIngreso.objects.filter(id_ingreso=id_ingreso, producto=p.producto.id)
        for producto in productos:
            variable = str(producto.id)
            print('Producto.id '+variable)
            print(str(producto.precio_compra))
            #Haciendo un codigo dinamico
            codigo_generado = User.objects.make_random_password(length=8, allowed_chars='123456789')
            print(codigo_generado)
            while Stock.objects.filter(codigo=codigo_generado):
                codigo_generado = User.objects.make_random_password(length=8, allowed_chars='123456789')
                print(codigo_generado)

            print(codigo_generado)
            nuevo = Stock()
            nuevo.producto = Producto.objects.get(pk=p.producto.id)
            nuevo.cantidad = producto.cantidad
            nuevo.precio_venta = producto.precio_venta
            nuevo.precio_descuento = producto.precio_descuento
            nuevo.codigo = codigo_generado
            nuevo.save()

#Al vender productos
