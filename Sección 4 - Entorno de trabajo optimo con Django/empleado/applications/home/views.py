from django.shortcuts import render

# 
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView 
)
# import models
from .models import Prueba

class PruebaView(TemplateView):
    template_name = "home/prueba.html"
    
    
class PuebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listanumeros'
    queryset = ['0', '10', '20', '30']   
    
    
class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'
    

class PruebaCreateView(CreateView):
    template_name = "home/add.html"    
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad']
    