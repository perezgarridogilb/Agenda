
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
        print(usuario)
        return Product.objects.productos_por_user(usuario)

class ListProductStok(ListAPIView):
    serializer_class = ProductSerializer 
    # Paquete drescifra token 
    # Autentica que el token le pertenece a un usuario
    authentication_clases = (TokenAuthentication,) 
    
    # [IsAuthenticated, IsAdminUser]: Autenticación para usuarios administradores 
    # Interfiere si se carga o no se carga 
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self): 
        # recuperando usuario
        return Product.objects.productos_con_stok()
    
class ListProductGenero(ListAPIView):
    serializer_class = ProductSerializer 
        
    def get_queryset(self): 
        # recuperando usuario 
        genero = self.kwargs['gender']
        return Product.objects.productos_por_genero(genero)

