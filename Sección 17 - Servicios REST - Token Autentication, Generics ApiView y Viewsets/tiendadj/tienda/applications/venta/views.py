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
#
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
    """  """

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        # inicalizamos valores
        amount = 0 # monto total de venta
        count = 0
        # registramos la venta
        venta = Sale.objects.create(
            date_sale=timezone.now(),
            amount=amount,
            count=count,
            type_invoce=serializer.validated_data['type_invoce'],
            type_payment=serializer.validated_data['type_payment'],
            adreese_send=serializer.validated_data['adreese_send'],
            state='3',
            user=self.request.user,
        )
        # recuperamos los productos de la venta
        productos = serializer.validated_data['productos']
        # para cada producto regustramos una venta detalle
        ventas_detalle = []
        for producto in productos:
            # recuperamos producto
            prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale=venta,
                product=prod,
                count=producto['count'],
                price_purchase=prod.price_purchase,
                price_sale=prod.price_sale,
            )
            #
            ventas_detalle.append(venta_detalle)
            #
            amount = amount + prod.price_sale
            count = count + producto['count']
        #
        venta.amount = amount
        venta.count = count
        #
        SaleDetail.objects.bulk_create(ventas_detalle)
        return Response({'res': 'exitosos'})