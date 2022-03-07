from django.shortcuts import render

# 
from django.views.generic import (
    ListView,
    DetailView
)

from .models import Entry, Category

class EntryListView(ListView):
    # template_name = "TEMPLATE_NAME"
    template_name = "entrada/lista.html"
    # Iteramos sobre este contexto
    context_object_name = 'entradas'
    # Páginado de diez en diez a nuestra lista de entradas
    paginate_by = 10
    
    # Para enviar el contexto de vistas basadas en clases usamos get_context_data
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context
    
    
    def get_queryset(self): 
        # Proceso de búsqueda
        # Recuperando el kword desde el html (method=GET)
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')
        # Consulta de búsqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado
    
class EntryDetailView(DetailView):
    template_name = "entrada/detail.html"
    model = Entry 
