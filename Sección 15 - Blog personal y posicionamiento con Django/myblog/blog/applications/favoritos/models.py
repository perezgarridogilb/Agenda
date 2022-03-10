from tkinter import Entry
from django.db import models 
from django.conf import settings

# Apps de terceros
from model_utils.models import TimeStampedModel 
# Create your models here.

from applications.entrada.models import Entry

from .managers import FavoritesManager

class Favorites(TimeStampedModel): 
    """ Modelo para favoritos """
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='user_favorites', 
        on_delete=models.CASCADE, 
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites', 
        on_delete=models.CASCADE
    )
    
    objects = FavoritesManager()
    
    class Meta:
        # Resguardar el guardado doble de un Usuario y una entrada 
        unique_together = ('user', 'entry') 
        verbose_name = 'Entrada Favorita' 
        verbose_name_plural = 'Entradas Favoritas'
        
    def __str__(self):
        return self.entry.title
        