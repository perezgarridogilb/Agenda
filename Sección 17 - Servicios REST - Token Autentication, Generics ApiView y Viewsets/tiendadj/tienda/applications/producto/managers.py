from django.db import models 

class ProductManager(models.Manager): 
    
    def productos_por_user(self, usuario): 
        return self.filter( 
            user_created=usuario,
        )
        
    def productos_con_stok(self): 
        return self.filter( 
            stok__gt=0,
            # Enumerar por el número de ventas
        ).order_by('-num_sales') 
        
    def productos_por_genero(self, genero): 
        # lista produtos por genéro 
        if genero == 'm': 
            mujer = True 
            varon = False
        elif genero == 'v': 
            varon = True 
            mujer = False 
        else: 
            varon = True 
            mujer = True 
            
        return self.filter( 
            woman=mujer, 
            man=varon               
        ).order_by('created')    
    
    # **filtros: Recibiendo varios parámetros con un diccionario de Python    
    def filtrar_productos(self, **filtros): 
        return self.filter( 
          man=filtros['man'], 
          woman=filtros['woman'], 
          name__icontains=filtros['name']  
        )     
