from rest_framework import viewsets
from rest_framework.response import Response

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
    
    # def create(self, request): 
    #     print(request.data) 
    #     return Response({'code': 'exitosos'}) 
    
    def perfom_create(self, serializer): 
        serializer.save(
            video="https://a.com/1/"
        )
        
    def list(self, request, *args, **kwargs): 
        queryset = Product.objects.productos_por_user(self.request.user)
        # 
        serializer = self.get_serializer(queryset, many=True) 
        return Response(serializer.data)    