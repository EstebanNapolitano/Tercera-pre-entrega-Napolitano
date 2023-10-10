from django.contrib import admin
from .models import *
from .models import Avatar

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombredeproyecto', 'descripcion', 'miembro', 'mostrar_tareas_asociadas')

    def mostrar_tareas_asociadas(self, obj):
        tareas = obj.tareas_asociadas()
        tareas_str = ', '.join([t.nombredetarea for t in tareas])
        return tareas_str

    mostrar_tareas_asociadas.short_description = 'Tareas Asociadas'

class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombredetarea', 'estado', 'proyecto_nombre', 'mostrar_proyectos_asociados')

    def proyecto_nombre(self, obj):
        return obj.proyecto.nombredeproyecto if obj.proyecto else ''

    def mostrar_proyectos_asociados(self, obj):
        proyectos = obj.proyectos_asociados()
        proyectos_str = ', '.join([p.nombredeproyecto for p in proyectos])
        return proyectos_str

    proyecto_nombre.short_description = 'Proyecto'
    mostrar_proyectos_asociados.short_description = 'Proyectos Asociados'

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Miembro)
admin.site.register(Avatar)

