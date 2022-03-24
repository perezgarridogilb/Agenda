from django.shortcuts import render

from rest_framework.generics import ( 
    ListAPIView, 
    CreateAPIView                                
)
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# 
from .models import Sale, SaleDetail
# serializado 
from .serializers import (
    VentaReporteSerializers, 
    ProcesoVentaSerializer

)    

class ReporteVentasList(ListAPIView): 
    
    serializer_class = VentaReporteSerializers 
    
    def get_queryset(self):
        return Sale.objects.all()

class RegistrarVenta(CreateAPIView): 
    # Paquete drescifra token 
    authentication_clases = (TokenAuthentication,) 
    # Tipos de permisos en base a la autenticación 
    permission_classes = [IsAuthenticated] 
    
    # Serializador
    serializer_class = ProcesoVentaSerializer 
    
    # Sobreescribiendo método create
    def create(self, request, *args, **kwargs): 
        serializer = ProcesoVentaSerializer(data=request.data) 
        # Verifica que lo que viene en el serializador "sea válido".
        serializer.is_valid(raise_exeption=True) 
        # type_invoce: Dato tipo recibo
        tipo_recibo = serializer.validate_data['type_invoce'] 
        print(5*'*', tipo_recibo) 
        return None
