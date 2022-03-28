from rest_framework import viewsets

from .models import Colors, Product
# 
from .serializers import (
    ColorsSerializer, 
    ProductSerializer, 
    PaginationSerializer, 
    ProductSerializerViewSet
)

class ColorViewSet(viewsets.ModelViewSet): 
    # Trabajar crud con
    serializer_class = ColorsSerializer 
    queryset = Colors.objects.all() 
    
class ProductViewSet(viewsets.ModelViewSet): 
    # Trabajar crud con
    serializer_class = ProductSerializerViewSet 
    queryset = Product.objects.all() 
    pagination_class = PaginationSerializer
        