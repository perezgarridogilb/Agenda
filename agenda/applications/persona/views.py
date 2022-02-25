from pipes import Template
from re import template
from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import ListAPIView

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