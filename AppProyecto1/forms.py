from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar, Tarea, Proyecto


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
    subtitulo = forms.CharField(max_length=100, required=False)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    fechaDeCreacion = forms.DateField(required=False)
    imagen = forms.ImageField(required=False)



class MiembroFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)


class BusquedaFormulario(forms.Form):

    criterio = forms.CharField(max_length=100, required=True, label='Ingrese su criterio de búsqueda')

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("email", "username", "password1", "password2")

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden, por favor revise e intente nuevamente")
        return password2
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text="")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)