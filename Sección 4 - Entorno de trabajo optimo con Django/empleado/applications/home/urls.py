from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # Forma en Django de estar ejecutando vistas genéricas
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PuebaListView.as_view()),
]