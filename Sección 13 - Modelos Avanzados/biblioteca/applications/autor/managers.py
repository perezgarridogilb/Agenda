from django.db import models

# La Q nos ayuda a implementar sentencias de tipo or
from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para el modelo autor """ 
    
    def buscar_autor(self, kword):
        # self: Autor.objects
        resultado = self.filter(
            # nombre o nombre__icontains (no exactamente iguales)
            nombre__icontains=kword
        )

        
        return resultado
    
    
    def buscar_autor1(self, kword):
            
            # Quiero que filtres a las instancias, cuyo kword sea similar al que estoy enviando o el apellido sea igual al kword que estoy enviando
        resultados = self.filter(Q(nombre__icontains=kword) | Q(nombre__icontains=kword))

        
        return resultados    
    
    def buscar_autor2(self, kword):
            
            # Quiero que filtres a las instancias, cuyo kword sea similar al que estoy enviando o el apellido sea igual al kword que estoy enviando
        resultados = self.filter(
            nombre__icontains=kword
            ).exclude(Q(edad__icontains=33) | Q(edad__icontains=46))

        
        return resultados    
    
    def buscar_autor3(self, kword):
            
            # Quiero que filtres a las instancias, cuyo kword sea similar al que estoy enviando o el apellido sea igual al kword que estoy enviando
        resultados = self.filter(
            edad__gt=40,
            edad__lt=65
            ).order_by('apellidos', 'nombre', 'id')

        
        return resultados