from django.conf.urls import url

from .views import *

urlpatterns = [
    #Urls para vender
    url('^$', VentasRapidas.as_view(), name='Ventas'),
    url('^vender/$', terminarVenta, name='Vender'),
    url('^terminar/$', vender, name='Terminar ventas'),
    #url('^venta/$', vender,  name="Vendiendo"),
    #url('^$', VentasRapidas.as_view(), name="Ventas rapidas"),
    #url('^venta/$', ventaBus),
    #url('^buscado/$', buscar, name='busqueda'),
]
