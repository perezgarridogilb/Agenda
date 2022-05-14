from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # Forma en Django de estar ejecutando vistas genéricas
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
]