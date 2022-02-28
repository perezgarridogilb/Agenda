from pipes import Template
from re import template
from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    )

from .models import Person, Reunion

from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer1,
    ReunionSerializer,
    PersonaSerializer2, 
    ReunionSerializerLink
)

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
    
class PersonUpdateView(UpdateAPIView):
    # El serializardor, con el cual va a recibir los datos
    serializer_class = PersonSerializer
    
    # Deacuerdo al pk que queremos encontrar en el enlace
    queryset = Person.objects.all()   
    
class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    # El serializardor, con el cual va a recibir los datos
    serializer_class = PersonSerializer
    
    # Deacuerdo al pk que queremos encontrar en el enlace
    queryset = Person.objects.all()
    
class PersonApiLista(ListAPIView):
    """
        Vista para interactuar con serializadores
    """
    # Cuando intentemos serializar algo siempre el serializador va a recibir un queryset
    # Ya sea un queryset de un sólo elemento:
    # Tiene que ser un elemento con determinada estructura
    # 
    # serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer2
    
    def get_queryset(self):
        # Si se intenta serializar esto:
        # lista_aux = ['Juan', 'Pedro']
        # return lista_aux
        
        # Va a determinar un error
        # Ya sea un serializador conectado a un modelo / manual
        # Espera un objeto que tenga estas caracteristicas:
        # id = serializers.IntegerField(), full_name = serializers.CharField(), job = serializers.CharField(), ..., n  
        return Person.objects.all()
    
class ReunionApiLista(ListAPIView):
    """
        Vista para interactuar con serializadores
    """
    
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
         
        return Reunion.objects.all()    
    
class ReunionApiListaLink(ListAPIView):
    """
        Vista para interactuar con serializadores
    """
    
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
         
        return Reunion.objects.all()     