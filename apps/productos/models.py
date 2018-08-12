from django.db import models

#from apps.proveedor.models import Proveedor
#from apps.local.models import Local, StockLocal

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

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.producto


class Ingreso(models.Model):
    proveedor = models.ForeignKey('proveedor.Proveedor', on_delete=models.PROTECT, default=1)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    local = models.ForeignKey('local.Local', on_delete=models.PROTECT, default=1)
    descripcion = models.CharField(max_length=200, default='Descripcion del ingreso')

    def __str__(self):
        return self.proveedor+' '+self.local

class DetalleIngreso(models.Model):
    id_ingreso = models.ForeignKey(Ingreso, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
    precio_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    codigo_producto = models.CharField(max_length=6)

    def __str__(self):
        return self.producto

class Envio(models.Model):
    local_salida = models.CharField(default='Local Principal', max_length=30)
    local_llegada = models.ForeignKey('local.Local', on_delete=models.PROTECT, default=1)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)

    def __str__(self):
        return 'De '+self.local_salida+' a '+self.local_llegada

class DetalleEnvio(models.Model):
    id_envio =  models.ForeignKey(Envio, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()

class Venta(models.Model):
    local = models.ForeignKey('local.Local', on_delete=models.PROTECT, default=1)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    cedula = models.CharField(max_length=10, default='9999999999')
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.local

class DetalleVenta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey('local.StockLocal', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
