from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^venta/$', vender,  name="Vendiendo"),
]
