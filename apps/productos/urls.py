from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.Productos.as_view(), name='Lista productos'),
    url('^ingresar/', views.IngresarProducto.as_view(), name='Ingresar producto'),

    url('^ingresos/$', views.Ingresos.as_view(), name='Lista ingresos'),
    url('^ingresos/ingresar/$', views.IngresarIngreso.as_view(), name='Ingreso de ingresos'),
    url('^ingresos/detalles/$', views.DetallesIngreso.as_view(), name='Detalles ingreso'),

    url('^envios/$', views.Envios.as_view(), name='Lista envios'),
    url('^envios/ingresar/$', views.IngresarEnvio.as_view(), name='Ingresar envio'),
    url('^envios/detalles/$', views.DetallesEnvio.as_view(), name='Detalles envio'),

]
