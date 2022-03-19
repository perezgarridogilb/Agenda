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