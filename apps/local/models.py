from django.db import models

# Create your models here.

class Local(models.Model):
	nombre = models.CharField(max_length=40, unique=True)
	direccion = models.CharField(max_length=40)
	telefono = models.CharField(max_length=9)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = 'Locales'

class StockLocal(models.Model):
	local = models.ForeignKey(Local, on_delete=models.CASCADE)
	producto = models.ForeignKey('productos.DetalleIngreso', on_delete=models.CASCADE)
	cantidad = models.PositiveIntegerField()
	precio_venta = models.DecimalField(max_digits=5, decimal_places=2)
	precio_descuento = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.producto
