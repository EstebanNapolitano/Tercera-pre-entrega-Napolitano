from django.db import models

# Create your models here.
class Tarea (models.Model):

    ESTADO_CHOICES = (
        ('TO DO', 'To Do'),
        ('WIP', 'Work in Progress'),
        ('DONE', 'Done'),
    )

    nombredetarea = models.CharField(max_length=40)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'{self.nombredetarea} - {self.estado}'
    
class Proyecto (models.Model):
    
    nombredeproyecto = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombredeproyecto} - {self.descripcion}'

class Miembro (models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}'
    