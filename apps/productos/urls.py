from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.Productos.as_view(), name='Lista productos'),
    url('^ingresar/', views.IngresarProducto.as_view(), name='Ingresar producto'),
    url('^editar/(?P<pk>[\w-]+)/$', views.ProductosUpdate.as_view(), name='Editar'),

    url('^categorias/$', views.Categorias.as_view(), name='Categorias'),
    url('^categorias/editar/(?P<pk>[\w-]+)/$', views.CategoriaUpdate.as_view(), name='Editar categoria'),
    url('^categorias/ingresar/$', views.IngresarCategoria.as_view(), name='Ingresar caterogia'),

    url('^ingresos/$', views.Ingresos.as_view(), name='Lista ingresos'),
    url('^ingresos/ingresar/$', views.IngresarIngreso.as_view(), name='Ingreso de ingresos'),
    url('^ingresos/detalles/$', views.DetallesIngreso.as_view(), name='Detalles ingreso'),

    url('^enviar/$', views.Enviar.as_view(), name='Enviar'),
    url('^envios/$', views.Envios.as_view(), name='Envios'),

]
