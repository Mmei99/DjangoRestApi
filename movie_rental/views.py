from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import generics,status
from Movies import models
from . import serializers
from django.http import JsonResponse
from rest_framework import views
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User,Movie_Rental,Rental

from django.contrib.sites.shortcuts import get_current_site
import jwt
from drf_yasg import openapi
from decouple import config
from .serializers import Movie_RentalSerializer





class Movies_get_by_category(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny,]
    serializer_class = Movie_RentalSerializer
    @swagger_auto_schema(operation_summary="Get movies by category")
    def post(self,request,category):
       
            
        movies=Movie_Rental.objects.filter(category=category)

        #serialize them
        serializer=self.serializer_class(movies,many=True)
        
        #return json
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)