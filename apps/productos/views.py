from django.shortcuts import render
from django.views.generic import View, CreateView,\
    ListView, UpdateView, DetailView, DeleteView

from django.shortcuts import render, redirect,\
    render_to_response, HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.

class IngresarProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    succes_url = '//'

class Productos(ListView):
    model = Producto
    queryset = Producto.objects.all()
    template_name = 'productos/productos_list.html'
    context_object_name = 'productos'

class IngresarIngreso(CreateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'productos/ingreso_form.html'
    succes_url = '/ingresos/'

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

    def for_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        #Aqui debe ir una funcion que me ingrese
        #el codigo que le corresponde al producto
        formset.save()
        #Aqui deberia ir una funcio que me actualice
        #mi inventario
        return HttpResponseRedirect(self.succes_url)

    def for_invalid(self, form, formset):
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
