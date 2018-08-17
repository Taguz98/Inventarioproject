from django.db import models

#from apps.proveedor.models import Proveedor
#from apps.local.models import Local, StockLocal
#Debe a ver un campo en en el que ingresen en donde
#esta ubicado el producto, pero no se en donde ponerlo

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    stock_minimo = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

#Puede hacerce con consultas, investigar
class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    precio_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    codigo = models.CharField(max_length=8, unique=True, primary_key=True)

    def __str__(self):
        producto = (str(self.producto))
        return self.codigo

class Ingreso(models.Model):
    proveedor = models.ForeignKey('proveedor.Proveedor', on_delete=models.PROTECT, default=1)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    local = models.ForeignKey('local.Local', on_delete=models.PROTECT, default=1)
    descripcion = models.CharField(max_length=200, default='Descripcion del ingreso')

    def __str__(self):
        retorno = (str(self.proveedor) +' '+ str(self.local))
        retorno = (str(self.id))
        return retorno

class DetalleIngreso(models.Model):
    id_ingreso = models.ForeignKey(Ingreso, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    precio_descuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.producto

#Debo ingresar  el default correcto al resetear mi base de datos a 0
class Envio(models.Model):
    local_envio = models.ForeignKey('local.Local', on_delete=models.PROTECT, related_name="%(class)s_envio")
    local_llegada = models.ForeignKey('local.Local', on_delete=models.PROTECT, related_name="%(class)s_llegada")
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    producto = models.ForeignKey(Stock, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100, default='Sin ubicacion')

    def __str__(self):
        return self.id
