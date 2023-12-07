from django.contrib import admin
from .models import Servicio, Tipo, Equipo, Inventario, Recomendacion, DetalleRecomendacion

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Tipo)
admin.site.register(Equipo)
admin.site.register(Inventario)
admin.site.register(Recomendacion)
admin.site.register(DetalleRecomendacion)