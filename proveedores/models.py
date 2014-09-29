from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now=True)
