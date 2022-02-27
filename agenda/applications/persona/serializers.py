import email
from rest_framework import serializers

from .models import Hobby, Person, Reunion, Hobby

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
    
class PersonaSerializer1(serializers.ModelSerializer):
    
    activo = serializers.BooleanField(default=False)
    
    class Meta:
        model = Person
        fields = ('__all__')
        
class ReunionSerializer(serializers.ModelSerializer):
    
    # Serializando todos los valores de persona
    persona = PersonSerializer()
    
    class Meta:
        # Serializador conectado al modelo
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            )              

class HobbySerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Hobby
        fields = ('__all__')

class PersonaSerializer2(serializers.ModelSerializer):

    # Que serialize y que tenga una colección, no un sólo elemento
    hobbies = HobbySerializer(many=True)

    class Meta: 
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
            )

class ReunionSerializer1(serializers.ModelSerializer): 
    
    # Una concatenación como un método adicional
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        # Serializador conectado al modelo
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            # Importante: Hace falta agregar aunque no pertenezca al modelo
            'fecha_hora'
            )              
    
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)
        