from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic import ListView, CreateView

from .models import *
from .forms import *

from apps.local.models import Local, StockLocal
# Create your views here.

class Ventas(ListView):
    model = Venta
    queryset = Venta.objects.all()
    template_name = 'ventas/venta_list.html'
    context_object_name = 'ventas'

class DetallesVenta(ListView):
    model = DetalleVenta
    queryset = DetalleVenta.objects.all()
    template_name = 'ventas/detalleVenta_list.html'
    context_object_name = 'detalles'

class IngresarVenta(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/venta_form.html'
    success_url = '/ventas/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DetalleVentaFormSet()
        return self.render_to_response(
            self.get_context_data(
                form = form,
                formset = DetalleVentaFormSet))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = DetalleVentaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        #Aqui deberia ir una funcio que me reste
        #los productos del stock
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, formset):
        return render_to_response(
            self.get_context_data(
                form = form,
                formset = DetalleVentaFormSet))

#Venta rapida

def vender(request):
    if request.method == 'POST':
        key = request.POST.get('codigo', None)
        if not codigo:
            return HttpResponse("Ingrese su codigo")

        producto = StockLocal.objects.filter(codigo=codigo)

        return render(request, 'ventas/ventaRapida_form.html', {'productos':producto})

    return render (request, 'ventas/ventaRapida_form.html', {})
    
