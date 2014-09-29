from django.db import models
from proveedores.models import Proveedor

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    proveedor = models.ForeignKey(Proveedor)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class ProductoCantidad(models.Model):
    producto = models.OneToOneField(Producto)
    cantidad = models.IntegerField()
    fecha_modificacion = models.DateTimeField(auto_now=True)

class ProductoPrecio(models.Model):
    producto = models.OneToOneField(Producto)
    precio = models.DecimalField(decimal_places=2, max_digits=19)
    fecha_modificacion = models.DateTimeField(auto_now=True)
