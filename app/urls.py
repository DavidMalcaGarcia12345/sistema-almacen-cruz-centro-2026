from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.login_usuario),
    path('enlace_panel_control_almacen/' , views.enlace_panel_control_almacen),
    path('enlace_tabla_horario/' , views.enlace_tabla_horario),
    path('enlace_registrar_horario/' , views.enlace_registrar_horario),
    path('logica_registrar_horario/' , views.logica_registrar_horario)
]