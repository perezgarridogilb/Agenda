#
from rest_framework import serializers

from .models import Sale, SaleDetail 

class VentaReporteSerializers(serializers.ModelSerializer): 
    """ serializador para ver las ventas en detalle """ 
    # Siempre a escribir su respectiva función
    productos = serializers.SerializerMethodField()
    
    class Meta: 
        model = Sale
        fields = (
            'id', 
            'date_sale', 
            'amount', 
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send', 
            'user', 
            'productos', 
        )

    def get_productos(self, obj): 
        # Consulta de los detalles 
        query = SaleDetail.objects.productos_por_venta(obj.id) 
        # data: Donde se encuentra el valor serializable
        productos_realizados = DetalleVentaProductoSerializer(query, many=True).data
        return productos_realizados 

# Mostrando toda la información anidada    
class DetalleVentaProductoSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = SaleDetail 
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale', 
        ) 
    
class ProductDetailSerializers(serializers.Serializer): 
    pk = serializers.IntegerField() 
    count = serializers.IntegerField()
       
class ProcesoVentaSerializer(serializers.Serializer): 
    
    type_invoce = serializers.CharField() 
    type_payment = serializers.CharField()   
    adreese_send = serializers.CharField()  
    productos = ProductDetailSerializers(many=True) 
    
#  ListFieldSerializer: Definir de qué tipo va a ser este arreglo (enteros/textos/números grandes/décimales/etc-))
#  

class ArrayIntegerSerializer(serializers.ListField): 
    
    child = serializers.IntegerField()
   
class ProcesoVentaSerializer1(serializers.Serializer): 
    
    type_invoce = serializers.CharField() 
    type_payment = serializers.CharField()   
    adreese_send = serializers.CharField()  
    productos = ArrayIntegerSerializer() 
    cantidades = ArrayIntegerSerializer()  
    
    def validate_type_invoce(self, value): 
        # value: Valor para el momento en el que esta sucediendo el proceso
        if value != '0': 
            raise serializers.ValidationError('Ingrese un valor correcto')
        return value
    
    def validate(self, data): 
        if data['type_payment'] != '0':
            raise serializers.ValidationError('Ingrese un valor correcto')
        return data
     