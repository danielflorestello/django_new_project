from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes/')
