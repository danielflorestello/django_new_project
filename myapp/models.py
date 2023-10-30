from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.nombre