from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    TemplateView
)

from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    # Esto ayudaría a ahorrar recursos para los servidores
    paginate_by=4
    ordering='first_name'
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
    
class ListaHabilidadesEmpleado(ListView):
    """ Lista de habilidades de un empleado """
    template_name = 'persona/habilidades.html'   
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        # Recupera un único registro de la Base de Datos 
        empleado = Empleado.objects.get(id=2)
        # print(empleado.habilidades.all())
        return empleado.habilidades.all()
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"    
    
    # Lo mismo de ListaHabilidadesEmpleado en get_queryset y ya no nos obliga escribirlo
    # A menos de intervenir
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Proceso
        context["Titulo"] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"
    success_url = reverse_lazy('persona_app:success')
    
    
class EmpleadoCreateView(CreateView):
        template_name = "persona/add.html"
        model = Empleado
        # Crea internamente las cajas de texto del prototipo presentado
        # fields = ['first_name', 'last_name', 'job']
        fields = [
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
        ]
        success_url = reverse_lazy('persona_app:success')
        
        
        def form_valid(self, form):
            # Lógica | commit=False
            empleado = form.save()
            empleado.full_name = empleado.first_name + ' ' + empleado.last_name
            empleado.save()
            return super(EmpleadoCreateView, self).form_valid(form)
        
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"        
    model = Empleado
    fields = [
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
        ]
    success_url = reverse_lazy('persona_app:success')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(5*"*")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Lógica
        print(5*"*")
        return super(EmpleadoUpdateView, self).form_valid(form)

# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
