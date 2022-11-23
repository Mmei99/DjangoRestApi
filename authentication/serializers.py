from rest_framework.validators import ValidationError
from .models import User
from rest_framework import serializers,status
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.ModelSerializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    email = serializers.EmailField(max_length=255,allow_blank=False,write_only=True)
    password = serializers.CharField(max_length=68,allow_blank=False,write_only=True)
    
    
    
    class Meta:
        model=User
        fields=['email','password']

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email','')
        password = attrs.get('password','')
        print(email,password)
        user=authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials login serializer")
        
        
        
        return super().validate(attrs)
        


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=40,allow_blank=False)
    email=serializers.EmailField(max_length=80,allow_blank=False)
    
    password=serializers.CharField(allow_blank=False)


    class Meta:
        model=User
        fields=['username', 'email','password']

    def validate(self,attrs):
        email=User.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username=User.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)


    def create(self,validated_data):
        

        return User.objects.create_user(**validated_data)
    
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=255)
    class Meta:
        model=User
        fields=['token']