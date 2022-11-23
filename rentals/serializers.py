from rest_framework import serializers
from .models import Movie,User
from .models import Rental
from store import settings



class RentalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Rental
        fields=['id','user_id','movie_id','created_at']
        
        
 