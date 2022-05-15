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

class ListEmpleadosByKword(ListView): 
    """ Lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print(5*"*")
        # Haciendo uso del objeto request
        palabra_clave = self.request.GET.get("kword", '')
        #print(5*'=', palabra_clave)
        lista = Empleado.objects.filter(
           # Atributo del atrito 
           first_name=palabra_clave
        )
        print('Lista resultado:', lista)
        return lista
    

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
