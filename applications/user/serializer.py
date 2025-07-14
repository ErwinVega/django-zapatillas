from rest_framework import serializers


from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    
    username= serializers.CharField()
    password= serializers.CharField()
    
    def validate(self, attrs):
        user = authenticate(username=attrs["username"],password=attrs["password"])
        if not user:
            raise serializers.ValidationError("credenciales no validas")
        attrs["user"]= user
        return attrs
    
    
    
