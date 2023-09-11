from django.urls import path
from .views import *
# Siempre utilizar app-proyecto1/ al final de http://127.0.0.1:8000/
urlpatterns = [
    path('',inicio, name="Inicio"),
    path('tareas/',tareas, name="Tareas"),
    path('agregar-tarea/', agregar_tarea, name='agregar-tarea'),
    path('proyectos/',proyectos, name="Proyectos"),
    path('agregar-proyecto/',agregar_proyecto, name='agregar-proyecto'),
    path('miembros/',miembros, name="Miembros"), 
    path('agregar-miembro/', agregar_miembro, name='agregar-miembro'),
    path('buscar/',buscar, name='buscar'),


]
