from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializer import (
    LoginSerializer
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import  PasswordResetTokenGenerator
# Create your views here.



class CreateTokenUser(APIView):
    
    
    def post(self,*args, **kwargs):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user:User= serializer.validated_data["user"]
        print(user)
        refresh = RefreshToken.for_user(user)
        return Response({
                "refresh":str(refresh),
                "access":str(refresh.access_token),
                "user":{
                    "id":user.id,
                    "username":user.username
                }
            })
            
       