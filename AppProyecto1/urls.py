from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from AppProyecto2.views import contacto_exito, contacto

# Siempre utilizar app-proyecto1/ al final de http://127.0.0.1:8000/
# user: Esteban pass: Teclado97
# user: admin pass: 123
urlpatterns = [
    path('',inicio, name="Inicio"),
    path('tareas/',tareas, name="Tareas"),
    path('agregar-tarea/', agregar_tarea, name='agregar-tarea'),
    path('proyectos/',proyectos, name="Proyectos"),
    path('agregar-proyecto/',agregar_proyecto, name='agregar-proyecto'),
    path('miembros/',miembros, name="Miembros"), 
    path('agregar-miembro/', agregar_miembro, name='agregar-miembro'),
    path('buscar/',buscar, name='buscar'),
    path('about/',about, name="about"),
    path('tarea/<int:tarea_id>/', detalle_tarea, name='detalle_tarea'),
    path('proyecto/<int:proyecto_id>/', detalle_proyecto, name='detalle_proyecto'),
    path('miembro/<int:miembro_id>/', detalle_miembro, name='detalle_miembro'),
    path('login/',loginView, name="Login"),
    path('register/',register, name="Registrar"),
    path('logout/',LogoutView.as_view(template_name="logout.html"), name="Cerrar sesion"),
    path('editar-perfil/',editarPerfil, name="editarPerfil"),
    path('agregar-avatar/',agregarAvatar, name="agregar-avatar"),
    path('contacto/', contacto, name='contacto'),
    path('app-proyecto1/contacto-exito/', contacto_exito, name='contacto-exito'),
    ]
# AGREGAR LOS CAMPOS QUE AGREGAMOS A PROYECTO, A TODOS LOS MODELOS, HACER EL VIDEO, SUBIR LOS CASOS, ACTUALIZAR REPO Y LISTO

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
