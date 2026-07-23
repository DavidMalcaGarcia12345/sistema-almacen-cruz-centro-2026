from django.contrib import admin
from .models import Tabla_Cambio_Material_Vehicular , Tabla_Hora_Extra , Tabla_Horario_Tecnico , Tabla_Inventario , Tabla_Recepcion_Material , Tabla_Salida_Material , Tabla_Tecnico_Mecanico

admin.site.register(Tabla_Cambio_Material_Vehicular)
admin.site.register(Tabla_Hora_Extra)
admin.site.register(Tabla_Horario_Tecnico)
admin.site.register(Tabla_Inventario)
admin.site.register(Tabla_Recepcion_Material)
admin.site.register(Tabla_Salida_Material)
admin.site.register(Tabla_Tecnico_Mecanico)
