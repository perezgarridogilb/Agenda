from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView
)

from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'
    
class ListByAreaEmpleado(ListView): 
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'
  
    # queryset = Empleado.objects.filter(
    #     departamento__name='contabilidad'
    # )
    
    def get_queryset(self):
        # Fuente: https://ccbv.co.uk/projects/Django/3.1/django.views.generic.list/ListView/
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
           # Atributo del atrito 
           departamento__short_name=area
        )
        return lista

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
