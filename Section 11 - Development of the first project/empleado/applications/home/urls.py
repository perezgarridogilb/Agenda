from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # Forma en Django de estar ejecutando vistas genéricas
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PuebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name="prueba_add"),
]