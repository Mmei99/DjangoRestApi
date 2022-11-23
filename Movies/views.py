from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics,status
from .models import Movie
from . import serializers
from .models import User
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.shortcuts import render,get_object_or_404
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

        
class Movies_List(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny,]
    serializer_class = MovieSerializer
    @swagger_auto_schema(operation_summary="Get a list of all the movies")
    def get(self,request):
    
        #get Movies
        movies=Movie.objects.all()

        #serialize them
        serializer=self.serializer_class(movies,many=True)
        
        #return json
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        
        
        
            
            
class Movies_get_by_category(ListCreateAPIView):
    permission_classes=[permissions.AllowAny,]
    serializer_class = MovieSerializer
    @swagger_auto_schema(operation_summary="Get movies by category")
    def get(self,request,category):
       
            
        movies=Movie.objects.filter(category=category)

        #serialize them
        serializer=self.serializer_class(movies,many=True)
        
        #return json
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        
        
        
                
class MovieDetailView(ListCreateAPIView):
    permission_classes=[permissions.AllowAny,]
    serializer_class = MovieSerializer
    @swagger_auto_schema(operation_summary="Get the details a movie")
    def get(self,request,name):
            
        movies=Movie.objects.get(name=name)

        #serialize them
        serializer=MovieSerializer(movies)
        
        #return json
        return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        
        
       


        