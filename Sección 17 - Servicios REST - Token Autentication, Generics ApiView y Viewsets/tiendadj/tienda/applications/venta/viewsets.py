from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# 
from applications.producto.models import Product

# 
from .serializers import ProcesoVentaSerializer1, VentaReporteSerializers

# 
from .models import Sale, SaleDetail

class VentasViewSet(viewsets.ViewSet):
    
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    # Al parecer no requiere especificar de la misma manera los serializers (deja de ser prioridad)
    
    # Sin el queryset nos causa error
    queryset = Sale.objects.all()
    
    # Sobreescribir los métodos que nosotros necesitemos
    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all()
        # Sin serializers
        return Response({'probando': 'viewsets'})
        
    def retrieve(self, request, pk=None):
        return Response({'probando': 'viewsets'})
    
    