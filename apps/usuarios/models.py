from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cedula = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + self.apellido
