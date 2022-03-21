from rest_framework import serializers 
# 
from .models import Product, Colors 

class ColorsSerializer(serializers.ModelSerializer): 
    
    # Meta para conectarse al modelo 
    class Meta: 
        model = Colors 
        fields = (
            'color', 
        )

class ProductSerializer(serializers.ModelSerializer): 
    
    # many: Más de un objeto 
    colors = ColorsSerializer(many=True)
    
    # Meta para conectarse al modelo 
    class Meta: 
        model = Product 
        fields = (
            'name', 
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'colors',
            'video',
            'stok',
            'num_sales',
        )