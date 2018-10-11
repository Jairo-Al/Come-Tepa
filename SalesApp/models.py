from django.db import models
from .util import unique_slug_generator
from  django.db.models.signals import pre_save
from django.urls import reverse
from django.db.models import Q
# Create your models here.


class ProductManager(models.Manager):

    def get_by_id(self, pk):
        qs = self.get_queryset().filter(pk=pk)
        if qs.count() == 1:
            return qs.first()
        return None

    @staticmethod
    def get_by_res(res):
        qs = productos.objects.all().filter(nombre_res='{}'.format(res))
        return qs

    def featured(self):
        return self.get_queryset().filter(featured=True)




class productos(models.Model):
    platillo           = models.CharField(max_length=120)
    descripcion        = models.TextField()
    precio             = models.DecimalField(decimal_places=2,max_digits=20, default = 39.99)
    imagen             = models.ImageField( null=True, blank=True)
    nombre_res         = models.CharField(max_length=120)
    featured           = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.nombre_res

class restaurantes(models.Model):
    nombre_res         = models.CharField(max_length=120)
    descripcion        = models.TextField()
    telefono           = models.IntegerField()
    domicilio          = models.CharField(max_length=120)
    correo             = models.EmailField(max_length=255, unique=True)
    logo               = models.ImageField( null=True, blank=True)
    slug               = models.SlugField(blank = True, unique=True)

    def __str__(self):
        return self.nombre_res

    def get_url(self):
        #return "/productos/{slug}/".format(slug=self.slug)
        return reverse("select", kwargs={"slug": self.slug})

def res_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(res_pre_save_receiver, sender=restaurantes)



