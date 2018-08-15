from django.conf.urls import url

from .views import vender, Productos

urlpatterns = [
    url('^finventa/$', vender, name='finventa'),
    url('^venta/$', Productos.as_view(), name='venta'),
]
