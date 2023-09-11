from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def inicio(req):
    return render (req, 'inicio.html')

def tareas(req):
    return render (req, 'tareas.html')

def miembros(req):
    return render (req, 'miembros.html')

def proyectos(req):
    return render (req, 'proyectos.html')

def agregar_tarea (req):
    print('method', req.method)
    print('POST', req.POST)

    if req.method =='POST':
        nuevatarea = TareaFormulario(req.POST)

        if nuevatarea.is_valid():
            data = nuevatarea.cleaned.data
            tarea = Tarea(nombredetarea=req.POST["nombredetarea"], estado=req.POST["estado"])
            tarea.save()

            return render(req, 'tareas.html')
    else:
        nuevatarea = TareaFormulario()
        return render(req, 'agregar-tarea.html')

def agregar_miembro(req):
    print('method', req.method)
    print('POST', req.POST)

    if req.method =='POST':
        nuevomiembro = MiembroFormulario(req.POST)

        if nuevomiembro.is_valid():
            data = nuevomiembro.cleaned.data
            miembro = Miembro(nombre=req.POST["nombre"]) 
            miembro.save()

            return render(req, 'miembros.html')
    else:
        nuevomiembro = MiembroFormulario()
        return render(req, 'agregar-miembro.html')
    
def agregar_proyecto(req):
    print('method', req.method)
    print('POST', req.POST)

    if req.method =='POST':
        nuevoproyecto = ProyectoFormulario(req.POST)

        if nuevoproyecto.is_valid():
            data = nuevoproyecto.cleaned.data
            proyecto = Proyecto(nombredeproyecto=req.POST["nombredeproyecto"],descripcion=req.POST["descripcion"]) 
            proyecto.save()

            return render(req, 'proyectos.html')
    else:
        nuevoproyecto = ProyectoFormulario()
        return render(req, 'agregar-proyecto.html') 

def buscar(request):
    tipo_busqueda = request.GET.get('tipo_busqueda')
    resultados = []

    if tipo_busqueda == 'tarea':
        resultados = Tarea.objects.all()
    elif tipo_busqueda == 'proyecto':
        resultados = Proyecto.objects.all()
    elif tipo_busqueda == 'miembro':
        resultados = Miembro.objects.all()

    return render(request, 'buscar.html', {'tipo_busqueda': tipo_busqueda, 'resultados': resultados})