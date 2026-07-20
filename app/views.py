from django.shortcuts import render , redirect
from django.http import HttpResponse

def login_usuario(request): 
    return render(request , 'login_usuario.html')

def enlace_usuario(request): # para ingresar antes de login tiene que crear usuario
    return render(request , 'registrar_usuario.html')

def enlace_panel_control_almacen(request):
    return render(request , 'panel_control_almacen.html')

def enlace_tabla_horario(request):
    return render(request , 'tabla_horario.html')

def enlace_registrar_horario(request): 
    return render(request , 'registrar_horario.html')

