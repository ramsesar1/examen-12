# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contraseña=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        
        usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
        usuario.set_contraseña(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, contraseña=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(correo, contraseña, **extra_fields)

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'telefono', 'direccion']

    def set_contraseña(self, contraseña):
        self.contraseña = make_password(contraseña)

    def check_contraseña(self, contraseña):
        return check_password(contraseña, self.contraseña)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def __str__(self):
        return self.nombre
