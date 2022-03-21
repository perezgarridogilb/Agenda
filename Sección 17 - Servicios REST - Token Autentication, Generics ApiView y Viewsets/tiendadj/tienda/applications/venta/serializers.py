#
from rest_framework import serializers

from .models import Sale, SaleDetail 

class VentaReporteSerializers(serializers.ModelSerializer): 
    """ serializador para ver las ventas en detalle """ 
    class Meta: 
        model = Sale
        fields = (
            'date_sale', 
            'amount', 
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send', 
            'user',
        )
