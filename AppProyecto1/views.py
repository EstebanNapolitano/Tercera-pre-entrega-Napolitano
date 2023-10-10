from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def inicio(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

@login_required(login_url='/app-proyecto1/login')
def tareas(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render (req, 'tareas.html', {"url_avatar": avatar.imagen.url})
    except:
        return render (req, 'tareas.html')

@login_required(login_url='/app-proyecto1/login')
def miembros(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render (req, 'miembros.html', {"url_avatar": avatar.imagen.url})
    except:
        return render (req, 'miembros.html')

@login_required(login_url='/app-proyecto1/login')
def proyectos(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        miembros = Miembro.objects.all()
        print(miembros)
        return render(req, 'proyectos.html', {"url_avatar": avatar.imagen.url, "miembros": miembros})
    except:
        return render(req, 'proyectos.html')

def about(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render (req, 'about.html', {"url_avatar": avatar.imagen.url})
    except:
        return render (req, 'about.html')

@login_required(login_url='/app-proyecto1/login')
def agregar_tarea(req):
    print('method', req.method)
    print('POST', req.POST)
    
    if req.method == 'POST':
        nuevatarea = TareaFormulario(req.POST)

        if nuevatarea.is_valid():
            data = nuevatarea.cleaned_data
            tarea = Tarea(nombredetarea=req.POST["nombredetarea"], estado=req.POST["estado"])
            tarea.save()

            return render(req, 'tareas.html')
    else:
        nuevatarea = TareaFormulario()
        return render(req, 'agregar-tarea.html')

    
@login_required(login_url='/app-proyecto1/login')
def agregar_miembro(req):
     print('method', req.method)
     print('POST', req.POST)

     if req.method =='POST':
        nuevomiembro = MiembroFormulario(req.POST)

        if nuevomiembro.is_valid():
            data = nuevomiembro.cleaned_data
            miembro = Miembro(nombre=req.POST["nombre"]) 
            miembro.save()

            return render(req, 'miembros.html')
     else:
        nuevomiembro = MiembroFormulario()
        return render(req, 'agregar-miembro.html')


@login_required(login_url='/app-proyecto1/login')
def agregar_proyecto(req):
    print('method', req.method)
    print('POST', req.POST)

    if req.method =='POST':
        nuevoproyecto = ProyectoFormulario(req.POST, req.FILES)

        if nuevoproyecto.is_valid():
            data = nuevoproyecto.cleaned_data
            miembro_id = req.POST.get("miembro")
            miembro = Miembro.objects.get(pk=miembro_id)

            proyecto = Proyecto(
                nombredeproyecto=data["nombredeproyecto"],
                subtitulo=data["subtitulo"],
                descripcion=data["descripcion"],
                miembro=miembro,
                fechaDeCreacion=data["fechaDeCreacion"],
                imagen=data["imagen"]
            ) 
            proyecto.save()

            return render(req, 'proyectos.html', {"miembros": Miembro.objects.all()})
    else:
        nuevoproyecto = ProyectoFormulario()
        return render(req, 'agregar-proyecto.html')

@login_required(login_url='/app-proyecto1/login')
def buscar(request):
    tipo_busqueda = request.GET.get('tipo_busqueda')
    resultados = []

    try:
        avatar = Avatar.objects.get(user=request.user.id)

        if tipo_busqueda == 'tarea':
            resultados = Tarea.objects.all()
        elif tipo_busqueda == 'proyecto':
            resultados = Proyecto.objects.all()
        elif tipo_busqueda == 'miembro':
            resultados = Miembro.objects.all()
    except Avatar.DoesNotExist:
        avatar = None

    return render(request, 'buscar.html', {'tipo_busqueda': tipo_busqueda, 'resultados': resultados, 'url_avatar': avatar.imagen.url if avatar else None})


def detalle_tarea(req, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    return render(req, 'detalle_tarea.html', {'tarea': tarea})

def detalle_proyecto(req, proyecto_id):
    proyecto = get_object_or_404 (Proyecto, pk=proyecto_id)
    return render(req, 'detalle_proyecto.html', {'proyecto': proyecto})

def detalle_miembro (req, miembro_id):
    miembro = get_object_or_404 (Miembro, pk=miembro_id)
    return render(req, 'detalle_miembro.html', {'miembro': miembro})
 
def loginView(req):

    if req.method == 'POST':
        
        miFormulario = AuthenticationForm (req, data=req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data ["username"]
            password = data ["password"]
            user = authenticate(username=usuario, password=password)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvendido {usuario}"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos, intente nuevamente"})
            
    else:
        miFormulario = AuthenticationForm()
        return render (req, "login.html", {"miFormulario": miFormulario})

def register(req):
    
    if req.method == 'POST':
        
        miFormulario = CustomUserCreationForm (req.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {miFormulario.cleaned_data['username']} creado con éxito"})
                        
    else:
        miFormulario = CustomUserCreationForm()
        return render (req, "registro.html", {"miFormulario": miFormulario})

@login_required(login_url='/app-proyecto1/login')
def editarPerfil(req):
    
    usuario = req.user
    if req.method =='POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.username = data["username"]
            usuario.password = data ["password"]
            usuario.email = data ["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render (req, "editarPerfil.html", {"mensaje": "Datos correctamente actualizados"})
        else:
            return render (req, "editarPerfil.html", {"miFormulario": miFormulario})
 
    else:
        miFormulario = UserEditForm(instance=usuario)
        return render (req, "editarPerfil.html",{"miFormulario": miFormulario, "id": usuario.id})

    
def agregarAvatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizado"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar-avatar.html", {"miFormulario": miFormulario})
  
    