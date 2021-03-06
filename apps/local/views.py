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
