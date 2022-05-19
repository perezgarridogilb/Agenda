from re import template
from django.shortcuts import render
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento

# Importando departamento
from .forms import NewDepartamentoForm

class NewDepartamento(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('***Estamos en el form valid***')
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname'],
        )
        depa.save()
    
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            departamento=depa
        )
        return super(NewDepartamento, self).form_valid(form)
