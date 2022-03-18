
from rest_framework.generics import ( 
     ListAPIView,                                
)
#
from django.shortcuts import render
# 
from .serializers import ProductSerializer
# 
from .models import Product

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer 
    
    def get_queryset(self): 
        return Product.objects.all()
