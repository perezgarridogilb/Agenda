from pipes import Template
from re import template
from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )

from .models import Person

from .serializers import PersonSerializer

class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()
    
class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = "persona/lista.html"
    
class PersonSearchApiView(ListAPIView): 
    serializer_class = PersonSerializer
       
    def get_queryset(self):
           # Retorna en base a un parámetro de búsqueda
           # Filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )
        
# Siempre recibimos serializadores
class PersonCreateView(CreateAPIView):
    # form_class = Formulario   
    
    # En su defecto necesitaría un JSON
    serializer_class = PersonSerializer   
    
class PersonDetailView(RetrieveAPIView):
     
    # Requiere saber de dónde lo va a recuperar 
    serializer_class = PersonSerializer
    # queryset = Person.objects.filter()
    queryset = Person.objects.all() 
    
class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()        