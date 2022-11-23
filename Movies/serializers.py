from rest_framework import serializers
from .models import Movie,User
from rest_framework import serializers,status
from store import settings
from rest_framework.validators import ValidationError


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie
        fields=['id','name','description','category']
        
        


class MovieCreationSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=40,allow_blank=False)
    category=serializers.CharField(max_length=40,allow_blank=False)
    
    description=serializers.CharField(max_length=40,allow_blank=False)


    class Meta:
        model=User
        fields=['username', 'email','password']

    def validate(self,attrs):
        name=Movie.objects.filter(name=attrs.get('name')).exists()

        if name:
            raise ValidationError(detail="Movie with this name exists",code=status.HTTP_403_FORBIDDEN)

        

        return super().validate(attrs)


    def create(self,validated_data):
        

        return Movie.objects.create(**validated_data)