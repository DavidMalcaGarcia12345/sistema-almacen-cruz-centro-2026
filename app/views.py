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

def logica_registrar_horario(request): 
    Id_tabla = request.POST['textId']
    Nombre_tabla = request.POST['textNombre']
    Fecha_inicio = request.POST['textFechaRegistro']
    Hora_inicio = request.POST['textHoraInicio']
    Hora_final = request.POST['textHoraSalida']
    Comentario = request.POST['textComentario']

    horario = Tabla_Horario_Tecnico.objects.create(
        Id_tabla_horario = Id_tabla,
        Nombre_tabla_horario = Nombre_tabla,
        Fecha_inicio_horario = Fecha_inicio,
        Hora_inicio_horario = Hora_inicio,
        Hora_final_horario = Hora_final,
        Comentario_horario = Comentario,
    )
    return redirect("/enlace_tabla_horario/")
