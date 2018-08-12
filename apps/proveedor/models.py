from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField('Direccion/Ciudad',max_length=40)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=40, blank=True, null=True)
    ruc = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre +' '+self.apellido

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Proveedores'


TIPO_CUENTAS_CHOICES = (
    ('AHORRO', 'Ahorro'),
    ('CORRIENTE', 'Corriente')
)

class CuentasProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    banco = models.CharField('Banco/Cooperativa', max_length=50)
    tipo_cuenta = models.CharField(choices=TIPO_CUENTAS_CHOICES, max_length=12)
    numero_cuenta = models.CharField('Numero cuenta', max_length=15)

    class Meta:
        ordering = ['proveedor']
