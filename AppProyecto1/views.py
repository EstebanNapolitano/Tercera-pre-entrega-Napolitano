from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarea
# Create your views here.

def tarea(req, nombredetarea, estado):
    
    tarea = Tarea(nombredetarea=nombredetarea, estado=estado)
    tarea.save()
    return HttpResponse(f"""
    <p>Tarea: {nombredetarea} - Estado: {estado} guardada exitosamente</p>
    """)