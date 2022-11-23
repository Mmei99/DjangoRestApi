from rest_framework import serializers
from .models import Movie,User
from .models import Rental,Movie_Rental
from store import settings



class Movie_RentalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie_Rental
        fields=['rental_id','movie_id']
        
        
 