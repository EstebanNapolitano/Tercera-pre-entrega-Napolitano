from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    path('contacto-exito/', views.contacto_exito, name='contacto-exito'),
]