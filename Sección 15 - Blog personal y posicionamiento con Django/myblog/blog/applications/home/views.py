import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

# Apps entrada
from applications.entrada.models import Entry

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Se quiere un contexto o palabra calve para la pantalla principal
        # Contexto de portada
        # Manager con el nombre entrada_en_portada
        context["portada"] = Entry.objects.entrada_en_portada()
        return context
    
