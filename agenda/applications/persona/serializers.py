import email
from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        # Indica cómo estructuraremos el JSON
        # Qué se brindará como servicio al que haga la petición a nuestro servidor
        # La forma en cómo recibiremos datos desde un aplicativo Frontend, ya sea JavaScript o una aplicación móvil
        model = Person
        fields = ( '__all__')

# Serializer que no necesariamente esté conectado al modelo 
# Del cual necesitaríamos construir todo manualmente
# Un tipo de campo que puede trabajar como un serializador es similar a los models       
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField() 
    job = serializers.CharField() 
    email = serializers.EmailField() 
    phone = serializers.CharField()
    
    # Puede suceder que requiramos atributos extras, para ello se usó el parámetro default = false, o en su defecto:
    activo = serializers.BooleanField(required=False)  
    # En caso de que no queramos que aparezca, el que lo tenga, aparece, el que no, no aparece en nuestro Frontend, en caso de que se lo envíen desde allí  
