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
        return self.nombredetarea
    
class Poyecto (models.Model):
    nombredeproyecto = models.CharField(max_length=40)

class Miembro (models.Model):
    nombre = models.CharField(max_length=40)
    