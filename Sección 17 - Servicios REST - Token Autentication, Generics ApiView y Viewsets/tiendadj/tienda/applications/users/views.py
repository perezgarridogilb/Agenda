#THIRD_PARTY_APPS
from firebase_admin import auth
#rest_framework
from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
#django import
from django.views.generic import TemplateView
#
from .models import User

# 
# Django import
from django.views.generic import TemplateView 


# Serializers 
from .serializers import LoginSocialSerializer 

# models 
from .models import User

class LoginUser(TemplateView): 
    template_name = "users/login.html"
    
class GoogleLoginView(APIView): 
    # Para recibir / mostrar recibimos un serializador 
    serializer_class = LoginSocialSerializer 
    
    # Sobreescribiendo el método POST 
    # Recogiendo la información que viene dentro del serializador 
    
    def post(self, request): 
        # O (serializer = LoginSocialSerializer(data=request.data)) de este
        serializer = self.serializer_class(data=request.data) 
        serializer.is_valid(raise_exception=True)
        # 
        id_token = serializer.data.get('token_id') 
        # 
        decoded_token = auth.verify_id_token(id_token) 
        #
        email = decoded_token['email'] 
        name = decoded_token['name'] 
        avatar = decoded_token['picture'] 
        verified = decoded_token['email_verified'] 
        # Usuario creado o recuperado
        usuario, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active': True
            }
        )
        # Devolviendo al frontend el token propio, nuestro
        if created: 
            token = Token.objects.create(user=usuario) 
        else: 
            token = Token.objects.get(user=usuario)
        
        # Objeto JavaScript
            
        userGet = { 
          'id': usuario.pk,
          'email': usuario.email, 
          'full_name': usuario.full_name, 
          'genero': usuario.genero, 
          'date_birth': usuario.date_birth,  
          'city': usuario.city         
        }          
                
        return Response( 
            { 
                'token': token.key, 
                'user': userGet         
            }
            )