from django import forms

class TareaFormulario(forms.Form):
    ESTADO_CHOICES = (
        ('TO DO', 'To Do'),
        ('WIP', 'Work in Progress'),
        ('DONE', 'Done'),
    )

    nombredetarea = forms.CharField(max_length=40)
    estado = forms.ChoiceField(choices=ESTADO_CHOICES)


class ProyectoFormulario(forms.Form):

    nombredeproyecto = forms.CharField(max_length=40)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)


class MiembroFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)


class BusquedaFormulario(forms.Form):

    criterio = forms.CharField(max_length=100, required=True, label='Ingrese su criterio de búsqueda')

