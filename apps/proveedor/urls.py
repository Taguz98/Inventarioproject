from django.conf.urls import url

from .views import *

urlpatterns= [
    url('^ingresar/$', IngresarProveedor.as_view(), name='Ingresando proveedor'),
    url('^cuentas/ingresar/$', IngresarCuenta.as_view(), name='Ingresar cuentas'),
    url('^$', Proveedores.as_view(), name='Lista proveedores'),
    url('^cuentas/$', IngresarCuenta.as_view(), name='Ingresar cuenta'),

]
