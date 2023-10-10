from django.db import models
from django.contrib.auth.models import User


class Miembro(models.Model):
    nombre = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Proyecto(models.Model):
    nombredeproyecto = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    miembro = models.ForeignKey(Miembro, null=True, default=None, on_delete=models.CASCADE)
    fechaDeCreacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='proyecto_imagenes/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombredeproyecto} - {self.descripcion}'
    
    def tareas_asociadas(self):
        return Tarea.objects.filter(proyecto=self)


class Tarea(models.Model):
    ESTADO_CHOICES = (
        ('TO DO', 'To Do'),
        ('WIP', 'Work in Progress'),
        ('DONE', 'Done'),
    )

    nombredetarea = models.CharField(max_length=40)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombredetarea} - {self.estado}'

    def __str__(self):
        return f'{self.nombredetarea} - {self.estado}'
    
    def proyectos_asociados(self):
        return Proyecto.objects.filter(tarea=self)

    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)