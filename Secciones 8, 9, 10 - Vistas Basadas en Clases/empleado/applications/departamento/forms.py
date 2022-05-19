from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=55)
    apellidos = forms.CharField(max_length=55)
    departamento = forms.CharField(max_length=55)
    shortname = forms.CharField(max_length=25)
