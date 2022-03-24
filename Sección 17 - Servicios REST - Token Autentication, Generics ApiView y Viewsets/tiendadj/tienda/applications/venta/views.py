from datetime import datetime
from django.utils import timezone
#
from django.shortcuts import render
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
#
from applications.producto.models import Product
# Serializado
from .serializers import (
    VentaReporteSerializers,
    ProcesoVentaSerializer,
  # ProcesoVentaSerializer2
)
#
from .models import Sale, SaleDetail

class ReporteVentasList(ListAPIView): 
    
    serializer_class = VentaReporteSerializers 
    
    def get_queryset(self):
        return Sale.objects.all()

class RegistrarVenta(CreateAPIView): 
    authentication_classes = (TokenAuthentication,) 
    
    # [IsAuthenticated, IsAdminUser]: Autenticación para usuarios administradores 
    # Interfiere si se carga o no se carga 
    permission_classes = [IsAuthenticated]
    
    # Serializador
    serializer_class = ProcesoVentaSerializer 
    
    # Sobreescribiendo método create
    def create(self, request, *args, **kwargs): 
        # serializer = ProcesoVentaSerializer(data=request.data) 
        # Verifica que lo que viene en el serializador "sea válido".
        serializer = ProcesoVentaSerializer(data=request.data) 
        
        """""" 
        # Primero tenemos que hacer esta validación
        serializer.is_valid(raise_exception=True)
        
        # Para hacer este
        # type_invoce: Dato tipo recibo
        tipo_recibo = serializer.validated_data['type_invoce'] 
        """"""
        
        print(5*'*', tipo_recibo) 
        return Response({'code':'ok'})
