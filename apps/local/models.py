from django.db import models

#Importanod el stock
from apps.productos.models import Stock

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
	producto = models.ForeignKey(Stock, on_delete=models.CASCADE)
	cantidad = models.PositiveIntegerField()
	ubicacion = models.CharField('Ubicacion producto',max_length=50)

	def __str__(self):
		producto = (str(self.producto))
		return producto
