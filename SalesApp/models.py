from django.db import models

# Create your models here.
class productos(models.Model):
    platillo           = models.CharField(max_length=120)
    descripcion        = models.TextField()
    precio             = models.DecimalField(decimal_places=2,max_digits=20, default = 39.99)
    imagen             = models.ImageField( null=True, blank=True)
    nombre_res         = models.CharField(max_length=120)
    featured           = models.BooleanField(default=False)

class restaurantes(models.Model):
    nombre_res         = models.CharField(max_length=120)
    descripcion        = models.TextField()
    telefono           = models.IntegerField()
    domicilio          = models.CharField(max_length=120)
    correo             = models.EmailField(max_length=255, unique=True)
    logo               = models.ImageField( null=True, blank=True)


    def __str__(self):
        return self.nombre_res