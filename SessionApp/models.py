from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self,email,nombre,domicilio,telefono,password=None, is_active=True, is_superuser = False, is_staff = False):
        if not email:
            raise ValueError("Usuarios deben tener correo electronico")
        if not password:
            raise ValueError("Usuarios deben tener contraseña")

        user_obj = self.model(
        email = self.normalize_email(email)
        )
        user_obj.domicilio  = domicilio
        user_obj.telefono   = telefono
        user_obj.nombre     = nombre
        user_obj.set_password(password)
        user_obj.active     = is_active
        user_obj.superuser  = is_superuser
        user_obj.staff      = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,email,password=None):
        user = self.create_user(
        email,
        password=password,
        is_staff = True
        )

    def create_superuser(self,email,password=None):
        user = self.create_user(
        email,
        password=password,
        is_superuser = True,
        is_staff=True
        )

class User(AbstractBaseUser):
    email              = models.EmailField(max_length=255, unique=True)
    nombre             = models.CharField(max_length=255)
    domicilio          = models.CharField(max_length=255)
    telefono           = models.IntegerField(default = 378)
    active             = models.BooleanField(default=True)
    superuser          = models.BooleanField(default=False)
    staff              = models.BooleanField(default=False)
    USERNAME_FIELD     = 'email'

    def __str__(self):
        return self.email

    def has_perm(self,perm ,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.staff

    objects = UserManager()