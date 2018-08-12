from django.conf.urls import url

from .views import *

urlpatterns= [
    url('^ingresar/$', IngresarProveedor.as_view(), name='Ingresando proveedor'),
    url('^cuenta/ingresar/$', IngresarCuenta.as_view(), name='Ingresar cuentas'),

]
