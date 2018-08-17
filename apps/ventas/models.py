from django.db import models

# Create your models here.

#Final de factura
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

#Venta rapida
class VentaRapida(models.Model):
    local = models.ForeignKey('local.Local', on_delete=models.PROTECT)
    producto = models.ForeignKey('local.StockLocal', on_delete=models.PROTECT)
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
