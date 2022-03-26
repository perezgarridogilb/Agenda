from rest_framework import viewsets

from .models import Colors
#
from .serializers import ColorsSerializer

class ColorViewSet(viewsets.ModelViewSet): 
    # Trabajar crud con
    serializer_class = ColorsSerializer 
    queryset = Colors.objects.all() 
    