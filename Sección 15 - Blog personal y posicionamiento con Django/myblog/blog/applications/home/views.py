import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    # Para guardar la información del formulario 
    CreateView
)

# Apps entrada
from applications.entrada.models import Entry

# models
from .models import Home

# forms
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        # Recuperando el último registro de nuestro modelo home
        context["home"] = Home.objects.latest('created')
        # Se quiere un contexto o palabra calve para la pantalla principal
        # Contexto de portada
        # Manager con el nombre entrada_en_portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # Contexto para los artículos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # Entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # Enviamos formulario de suscripción
        context["form"] = SuscribersForm
        return context

class SuscriberCreateView(CreateView):
    # SuscribersForm ya está conectado al modelo y todo lo demás
    form_class = SuscribersForm 
    
    # CreateView solicita una url
    success_url = '.'   

# Requerimos que siempre reciba un html bajo el formato de este contact form
class ContactCreateView(CreateView):
    form_class = ContactForm 
    success_url = '.'   