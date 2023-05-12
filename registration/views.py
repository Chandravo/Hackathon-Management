
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings

from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *


# user registration view
class register(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(email,password)
        user.save()
        return Response({'status':'success'},status=status.HTTP_201_CREATED)
    
    
# user login view using JWT
class login(APIView):
    
    def post(self, request):
        
        try:
            data=request.data
            serializer = LoginSerializer(data=data)
            if (serializer.is_valid()):
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                print(email,password)
                user = authenticate(email=email, password=password)
                if user is None:
                    return Response({'error':'Invalid Credentials'},status=status.HTTP_400_BAD_REQUEST)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
                
            return Response({'status':'400','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

            
