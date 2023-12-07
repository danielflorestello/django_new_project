from django.db.models import Sum
from collections import defaultdict
from .models import Recomendacion, DetalleRecomendacion


class CBRAlgorithm:
    def obtener_recomendaciones(self, servicio_id, tipo_id):
        # Paso 1: Recuperación - Obtener casos similares de la base de datos
        casos_similares = Recomendacion.objects.filter(servicio_id=servicio_id, tipo_id=tipo_id)

        # Si no hay casos exactamente iguales, busca casos similares
        if not casos_similares:
             casos_similares = Recomendacion.objects.filter(servicio_id=servicio_id, tipo_id=tipo_id).distinct()

        # Paso 2: Reutilización - Obtener recomendaciones de casos similares
        recomendaciones = self.obtener_recomendaciones_casos_similares(casos_similares)

        return recomendaciones
    
    
    def obtener_recomendaciones_casos_similares(self, casos_similares):
        recomendaciones = defaultdict(list)

        for caso in casos_similares:
            detalles = DetalleRecomendacion.objects.filter(recomendacion=caso)

            # Calcular la similitud y priorizar casos con cantidad devuelta cercana a 0
            similitud = sum(detalle.cantidad_devuelta for detalle in detalles)

            # Almacenar los equipos y cantidades recomendadas para este caso
            for detalle in detalles:
                recomendaciones[caso].append({
                    'equipo_id': detalle.equipo,
                    'cod_sap': detalle.equipo.cod_sap,
                    'serie': detalle.equipo.serie,
                    'descripcion': detalle.equipo.descripcion,
                    'cantidad_recomendada': detalle.cantidad_recomendada,
                })

        # Ordenar las recomendaciones por similitud de menor a mayor
        recomendaciones = dict(sorted(recomendaciones.items(), key=lambda x: similitud))

        return recomendaciones
    
