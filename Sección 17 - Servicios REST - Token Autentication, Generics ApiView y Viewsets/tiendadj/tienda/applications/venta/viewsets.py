from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
# 
from django.utils import timezone
from django.shortcuts import get_list_or_404
# 
from applications.producto.models import Product

# 
from .serializers import ProcesoVentaSerializer1, VentaReporteSerializers

# 
from .models import Sale, SaleDetail

class VentasViewSet(viewsets.ViewSet):
    
    authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    # Al parecer no requiere especificar de la misma manera los serializers (deja de ser prioridad)
    
    # Sin el queryset nos causa error
    queryset = Sale.objects.all()
    
    def get_permissions(self):
        # AllowAny: Lo acceden todos los usuarios autenticados o no
        if(self.action=='list') or (self.action=='retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]    
    
    # Sobreescribir los métodos que nosotros necesitemos
    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all()
        # Sin serializers
        # many=True: Si no fueran varios, no se utiliza
        serializer = VentaReporteSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request): 
        serializer = ProcesoVentaSerializer1(data=request.data)  
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
        productos = Product.objects.filter( 
            # Consulta                               
            id__in=serializer.validated_data['productos']
        )
        #
        cantidades = serializer.validated_data['cantidades']
        # para cada producto regustramos una venta detalle
        ventas_detalle = []
        for producto, cantidad in zip(productos, cantidades):
            # recuperamos producto
            # prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale=venta,
                product=producto,
                count=cantidad,
                price_purchase=producto.price_purchase,
                price_sale=producto.price_sale,
            )
            #
            ventas_detalle.append(venta_detalle)
            #
            amount = amount + producto.price_sale*cantidad
            count = count + cantidad 
            # ventas_detalle.append(ventas_detalle)
        #
        venta.amount = amount
        venta.count = count
        venta.save()
        #
        SaleDetail.objects.bulk_create(ventas_detalle)
        return Response({'res': 'exitosos'}) 
        
    def retrieve(self, request, pk=None):
        # Recuperando el objeto venta
        # venta = Sale.objects.get(id=pk)
        venta = get_list_or_404(Sale.objects.all(), pk=pk)
        # Deserializando un objeto venta
        serializer = VentaReporteSerializers(venta)
        return Response(serializer.data)
    
    