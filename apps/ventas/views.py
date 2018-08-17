from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic import ListView, CreateView

from .models import *
from .forms import *

from apps.local.models import Local, StockLocal

from apps.productos.models import Stock
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

class VentasRapidas(ListView):
    model = VentaRapida
    queryset = VentaRapida.objects.all()
    template_name = 'ventas/ventaRapida_list.html'
    context_object_name = 'ventas'

def ventaBus(request):
    precio = request.GET.get('precio')
    cantidad = request.GET.get('cantidad')
    total = request.GET.get('total')
    print("******* Finalizo su venta *****")
    print(precio)
    print(cantidad)
    print(total)
    ultimaVenta = VentaRapida.objects.last()
    print("******")
    print(VentaRapida.objects.last())
    ultimaVenta.precio = precio
    ultimaVenta.cantidad = cantidad
    ultimaVenta.total = total
    ultimaVenta.save()
    RestarStockLocal(ultimaVenta.local, ultimaVenta.producto, cantidad)
    return render(request, 'ventas/busqueda.html')

def buscar(request):
    local = request.GET.get('local')
    codigo = request.GET.get('codigo')
    producto = StockLocal.objects.filter( local= local, producto=codigo)
    print(codigo)
    print(local)
    print(producto)
    print("------")
    print(StockLocal.objects.get(producto=codigo, local=local))
    nuevo = VentaRapida()
    nuevo.local = Local.objects.get(pk=local)
    nuevo.producto = StockLocal.objects.get(producto=codigo, local=local)
    nuevo.save()

    return render(request, 'ventas/encontrado.html',
                 {'productos':producto})


def RestarStockLocal(local, producto, cantidad):
    productoStock = Stock.objects.filter(codigo=producto)
    for stock in productoStock:
        cod = stock.codigo
        stock.cantidad = stock.cantidad - int(cantidad)
        stock.save()
        
    #Stock.objects.filter(codigo=producto).update(cantidad=cantidadStock-cantidad)
    print("/-/-/-/-/-/-/-")
    #cod = int(productoStock)
    print(cod)
    productoLocal = StockLocal.objects.filter(producto=cod, local=local)
    print(productoLocal)
    for pro in productoLocal:
        pro.cantidad = pro.cantidad - int(cantidad)
        pro.save()



"""    productolocal.cantidad = producto.cantidad - int(cantidad)
    productolocal.save()
    productostock.cantidad = stock.cantidad - int(cantidad)
    productostock.save()"""



"""def vender(request):
    if request.method == 'POST':
        key = request.POST.get('codigo', None)
        if not codigo:
            return HttpResponse("Ingrese su codigo")

        producto = StockLocal.objects.filter(codigo=codigo)

        return render(request, 'ventas/ventaRapida_term.html', {'productos':producto})

    return render (request, 'ventas/ventaRapida_form.html', {})
"""
