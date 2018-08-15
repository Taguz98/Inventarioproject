"""Inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

#Clases para venta y stock
from apps.productos.views import StockLista
#Clases de venta
from apps.ventas.views import IngresarVenta, Ventas, DetallesVenta
#Clase para consultar el inventario
from apps.local.views import StockLocales, StockLocalPrincipal, StockLocalTerminal, IngresarStockLocal,\
    Productos, vender

#Pruebas para vender

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^proveedor/', include('apps.proveedor.urls')),
    url('^productos/', include('apps.productos.urls')),

    #Urls para vender
    url('^vender/$', IngresarVenta.as_view(), name='Vender'),
    url('^ventas/$', Ventas.as_view(), name='Ventas'),
    url('^ventas/detalles/$', DetallesVenta.as_view(), name='Detalles ventas'),

    #Urls para consultar stock
    url('^stock/locales/$', StockLocales.as_view(), name='Stock general'),
    url('^stock/principal/$', StockLocalPrincipal.as_view(), name='Stock local principal'),
    url('^stock/terminal/$', StockLocalTerminal.as_view(), name='Stock local terminal'),
    url('^stock/locales/ingresar/$', IngresarStockLocal.as_view(), name='Ingresar stock'),

    #Urls para stock
    url('^stock/$', StockLista.as_view(), name='Stock'),

    #Prueba Ventas
    url('^locales/', include('apps.local.urls')),
    #url('^venta/$', Productos.as_view(), name='venta'),
    #url('^venta/finventa/$', vender, name='Vender'),


]
