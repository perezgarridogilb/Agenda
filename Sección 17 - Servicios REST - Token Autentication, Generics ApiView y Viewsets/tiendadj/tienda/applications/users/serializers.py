
# 
from rest_framework import serializers 

# Puede ser reutilizable 
class LoginSocialSerializer(serializers.Serializer):
    
    token_id = serializers.CharField(required=True)
    