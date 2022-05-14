from enum import unique
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.forms import BooleanField

# Create your models here.
class Departamento(models.Model):
    # blank=True|unique=True
    name = models.CharField('Nombre', max_length=55)
    short_name = models.CharField('Nombre Corto', max_length=25, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'short_name')
    
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name