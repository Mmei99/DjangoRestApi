from django.urls import reverse
from rest_framework.response import Response
from rest_framework import generics,status
from Movies import models
from . import serializers
from rest_framework import views
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
import jwt
from drf_yasg import openapi
from decouple import config



#Register User
class UserSerializer(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer
    permission_classes=[permissions.AllowAny,]
    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self,request):
        data=request.data
        

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            
            serializer.save()
            
            user_data=serializer.data
            
            user=User.objects.get(email=user_data['email'])
            
            token=RefreshToken.for_user(user)
            
            """  To use email authentication
            current_site=get_current_site(request).domain
            
            relativeLink=reverse('email-verify')
            
            absurl='http://'+current_site+relativeLink+'?token='+str(token)
            
            email_body='Hi '+ user.username+" use link below to verify your email \n"  +absurl
            
            data={'email_body':email_body,'to_email':user.email,'email_subject':'Verify your email'}
            
            Util.send_email(data)"""
            
            return Response(user_data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
class LoginView(generics.GenericAPIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes=[permissions.AllowAny,]
    
    serializer_class=serializers.LoginSerializer
    
    
    @swagger_auto_schema(operation_summary="User login")
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
class VerifyEmail(views.APIView):
    serializer_class=serializers.EmailVerificationSerializer
    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Description',type=openapi.TYPE_STRING)
    
    
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token=request.GET.get('token')
        try:
            payload=jwt.decode(token,config('SECRET_KEY'))
            user=User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified=True
                user.save()
                
            
            return Response({'email ': 'succesfully activated'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error ': 'link expired'},status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error ': 'invalid token'},status=status.HTTP_400_BAD_REQUEST)
            

