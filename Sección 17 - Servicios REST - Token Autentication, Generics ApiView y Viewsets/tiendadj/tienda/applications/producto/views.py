
from rest_framework.generics import ( 
     ListAPIView,                                
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
#
from django.shortcuts import render
# 
from .serializers import ProductSerializer
# 
from .models import Product

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer 
    # Paquete drescifra token 
    authentication_clases = (TokenAuthentication,) 
    # Tipos de permisos en base a la autenticación 
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self): 
        # recuperando usuario
        print(5*"*")
        usuario = self.request.user
        return Product.objects.productos_por_user(usuario)
