from django.contrib import admin
from django.urls import path

# Para importar vistas
from . import views

urlpatterns = [
    path(
        'autores/', 
        views.ListAutores.as_view(),
        name='autores'
         ),
]
