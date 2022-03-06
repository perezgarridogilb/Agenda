from django.shortcuts import render

# 
from django.views.generic import (
    ListView
)

class EntryListView(ListView):
    # template_name = "TEMPLATE_NAME"
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    # Páginado de diez en diez a nuestra lista de entradas
    paginate_by = 10
    
    def get_queryset(self):
        return []
    

