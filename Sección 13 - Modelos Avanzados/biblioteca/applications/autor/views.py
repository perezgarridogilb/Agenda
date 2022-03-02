from django.shortcuts import render

from django.views.generic import ListView

# models local
from .models import Autor

# Create your views here.

class ListAutores(ListView): 
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'
    
    def get_queryset(self):
        # Recuperar lo que se está enviando a través del identificador kword 
        palabra_clave = self.request.GET.get("kword", '') # kword y tupla
        # El valor que estamos recogiendo de la caja de txt del html
        return Autor.objects.buscar_autor1(palabra_clave)
    

