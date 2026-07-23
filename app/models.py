from django.db import models

# Create your models here.
class  Tabla_Horario(models.Model):
    Id_tabla_horario = models.CharField(max_length=250)
    Nombre_tabla_horario = models.CharField(max_length=250)
    Hora_inicio_horario = models.TimeField()
    Hora_final_horario = models.TimeField()
    Comentario_horario = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_tabla_horario} - {self.Nombre_tabla_horario}"

class  Tabla_Hora_Extra(models.Model): 
    Id_tabla_hora_extra = models.CharField(max_length=250)
    Nombre_hora_extra = models.CharField(max_length=250)
    Fecha_hora_extra = models.DateField()
    Hora_inicio_extra = models.TimeField()
    Hora_final_extra = models.TimeField()
    Cantidad_hora_extra = models.CharField(max_length=250)
    Comentario_hora_extra = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_tabla_hora_extra} - {self.Nombre_hora_extra}"

class Tabla_Recepcion_Material(models.Model): 
    Id_recepcion_material = models.CharField(max_length=250)
    Fecha_recepcion_material = models.DateField()
    Nombre_empresa_recepcion_material = models.CharField(max_length=250)
    Nombre_material_recepcion_material = models.CharField(max_length=250)
    Numero_factura_recepcion_material = models.CharField(max_length=250)
    Codigo_recepcion_material = models.CharField(max_length=250)
    Cantidad_recepcion_material = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_recepcion_material} - {self.Fecha_recepcion_material}"

class Tabla_Salida_Material(models.Model):
    Id_tabla_salida_material = models.CharField(max_length=250)
    Fecha_salida_material = models.DateField()
    Nombre_salida_material = models.CharField(max_length=250)
    Descripcion_salida_material = models.CharField(max_length=250)
    Padron_salida_material = models.CharField(max_length=250)
    Cantidad_salida_material = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_tabla_salida_material} - {self.Fecha_salida_material} - {self.Padron_salida_material}"

class Tabla_Cambio_Material_Vehicular(models.Model):
    Id_cambio_cambio_material_vahicular = models.CharField(max_length=250)
    Fecha_registro_cambio_material_vehicular = models.DateField()
    Fecha_emision_cambio_material_vehicular = models.DateField()
    Fecha_vencimiento_cambio_material_vehicular = models.DateField()
    Padron_cambio_material_vehicular = models.CharField(max_length=250)
    Placa_cambio_material_vehicular = models.CharField(max_length=250)
    Cantidad_cambio_material_vehicular = models.CharField(max_length=250)
    Comentario_cambio_material_vehicular = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_cambio_cambio_material_vahicular} - {self.Fecha_registro_cambio_material_vehicular} - {self.Placa_cambio_material_vehicular}"

class Tabla_Inventario(models.Model):
    Id_tabla_inventario = models.CharField(max_length=250)
    Fecha_tabla_inventario = models.DateField()
    Nombre_tabla_inventario = models.CharField(max_length=250)
    Descripcion_tabla_inventario = models.CharField(max_length=250)
    Cantidad_tabla_inventario = models.CharField(max_length=250)
    Comentario_tabla_inventario = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_tabla_inventario} - {self.Fecha_tabla_inventario}"
    
class Tabla_Tecnico_Mecanico(models.Model):
    Id_tabla_tecnico_mecanica = models.CharField(max_length=250) 
    Fecha_tabla_tecnico_mecanica = models.DateField()
    Nombre_tabla_tecnico_mecanica = models.CharField(max_length=250)
    Placa_tabla_tecnico_mecanica = models.CharField(max_length=250)
    Padron_tabla_tecnico_mecanico = models.CharField(max_length=250)
    Trabajo_tabla_tecnico_mecanico = models.CharField(max_length=250)
    Comentario_tabla_tecnico_mecanico = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Id_tabla_tecnico_mecanica} - {self.Fecha_tabla_tecnico_mecanica} - {self.Padron_tabla_tecnico_mecanico}"
