import email
from tabnanny import verbose
from django.db import models
# Aplicaciones de terceros
from model_utils.models import TimeStampedModel 

class Home(TimeStampedModel):
    """ Model para datos de la pantalla home """
    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Título Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto', blank=True,
        null=True
    )
    phone = models.CharField(
        'Teléfono de contacto',
        max_length=20
    )
    
    class Meta:
        verbose_name = "Página principal"
        verbose_name_plural = "Página principal"
        
    def __str__(self):
        return self.title
    
    
class Suscribers(TimeStampedModel):    
    """ Suscripciones """    
    email = models.EmailField()
        
    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"
        
        
    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):   
    """ Formulario de Contacto """
    full_name = models.CharField(
        'Nombres',
        max_length=60
    ) 
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Mensajes"
        
    def __str__(self):
        return self.full_name
    