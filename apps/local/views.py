from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from django.views.generic import ListView, CreateView

from .models import *

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

class StockLocales(ListView):
    model = StockLocal
    queryset = StockLocal.objects.all().order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

#Los filtres deberia arreglarlos a la hora de programar
class StockLocalPrincipal(ListView):
    model = StockLocal
    queryset = StockLocal.objects.filter(local=3).order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

class StockLocalTerminal(ListView):
    model = StockLocal
    queryset = StockLocal.objects.filter(local=4).order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

class IngresarStockLocal(CreateView):
    model = StockLocal
    fields = ['local', 'producto', 'cantidad', 'ubicacion']
    success_url = '/stock/locales/'


#Pruebas para vender
from django.core import serializers
import json

from decimal import Decimal

class Productos(ListView):
    model = StockLocal
    queryset = StockLocal.objects.all()
    template_name = 'local/vender.html'
    context_object_name = 'productos'

#Clase sacada de stack

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)


def vender(request):
    #La busqueda me sale excelente de esta forma
    codigo = request.GET.get('cantidad')
    print(str(codigo))
    local = request.GET.get('local')
    print(local)
    productos = StockLocal.objects.filter(producto=codigo, local=local)
    productos = [ vender_serializer(producto) for producto in productos ]
    for producto in productos:
        print(producto)

    return HttpResponse(json.dumps(productos, content_type='application/json'))

def vender_serializer(producto):
    return {'producto':producto.producto.producto.nombre,
            'cantidad': producto.cantidad}

#'precio_venta': producto.producto.precio_venta,
