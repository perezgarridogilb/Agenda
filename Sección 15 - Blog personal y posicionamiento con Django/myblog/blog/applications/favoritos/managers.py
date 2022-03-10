# Importando models
from django.db import models 

class FavoritesManager(models.Manager):
    
    # Usuario como parámetro para poder hacer la consulta
    def entradas_user(self, usuario): 
        return self.filter(
            entry__public=True,
            user=usuario
        ).order_by('-created')