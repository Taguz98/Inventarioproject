from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from django.views.generic import ListView, CreateView

from .models import *

# Create your views here.

class StockLocales(ListView):
    model = StockLocal
    queryset = StockLocal.objects.all().order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

class StockLocalPrincipal(ListView):
    model = StockLocal
    queryset = StockLocal.objects.filter(local=1).order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

class StockLocalTerminal(ListView):
    model = StockLocal
    queryset = StockLocal.objects.filter(local=2).order_by('cantidad')
    template_name = 'local/stockLocales_list.html'
    context_object_name = 'stocks'

class IngresarStockLocal(CreateView):
    model = StockLocal
    fields = ['local', 'producto', 'cantidad', 'ubicacion']
    success_url = '/stock/locales/'


from django.core import serializers
import json

class Productos(ListView):
    model = StockLocal
    queryset = StockLocal.objects.all()
    template_name = 'local/vender.html'
    context_object_name = 'productos'

def vender(request):
    codigo = request.GET.get('codigo')
    productos = StockLocal.objects.filter(producto_id=codigo)
    productos = [ vender_serializer(producto) for producto in productos ]

    return HttpResponse(json.dumps(productos), content_type='application/json')

def vender_serializer(producto):
    return {'producto':producto ,'precio_venta':precio_venta,
            'cantidad':cantidad}
