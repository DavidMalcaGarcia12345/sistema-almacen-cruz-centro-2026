from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Tabla_Cambio_Material_Vehicular , Tabla_Hora_Extra , Tabla_Horario_Tecnico , Tabla_Inventario , Tabla_Recepcion_Material , Tabla_Salida_Material , Tabla_Tecnico_Mecanico

def login_usuario(request): 
    return render(request , 'login_usuario.html')

def enlace_panel_control_almacen(request):
    return render(request , 'panel_control_almacen.html')

def enlace_tabla_horario(request):
    tabla_horario = Tabla_Horario_Tecnico.objects.all()
    return render(request , 'tabla_horario.html' , {
        'tabla_horario' : tabla_horario
    })

def enlace_registrar_horario(request): 
    return render(request , 'registrar_horario.html')

