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
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = VentaReporteSerializers
    # Sin el queryset nos causa error
    queryset = Sale.objects.all()