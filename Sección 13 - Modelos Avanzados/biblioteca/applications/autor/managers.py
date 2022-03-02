from django.db import models

class AutorManager(models.Manager):
    """ Managers para el modelo autor """ 
    
    def buscar_autor(self, kword):
        # self: Autor.objects
        resultado = self.filter(
            # nombre o nombre__icontains (no exactamente iguales)
            nombre__icontains=kword
        )

        
        return resultado