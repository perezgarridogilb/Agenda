from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    # Forma en Django de estar ejecutando vistas genéricas
    path(
        '', 
        views.InicioView.as_view(), 
    name="inicio"
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(), 
        name="empleados_all"
    ),
    path(
        'listar-by-area/<shortname>/',
        views.ListByAreaEmpleado.as_view(),
        name="empleados_area"
    ),
    path(
        'listar-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name="empleados_admin"
    ),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name="empleado_detail"),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="add" ),
    path('success/', views.SuccessView.as_view(), name="success" ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name="modificar_empleado" 
    ),
    path('eliminar-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name="eliminar_empleado" ),
]