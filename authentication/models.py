from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password,**extra_fields):
        if not username:
            raise ValueError(_('Please enter a username'))
        if not email:
            raise ValueError(_('Please enter an email address'))
        if not password:
            raise ValueError(_('Please enter a password'))
        
        

        email=self.normalize_email(email)

        new_user=self.model(username=username,email=email)

        new_user.set_password(password)

        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True'))


        return self.create_user(email,password,**extra_fields)


class User(AbstractUser):
    id=models.AutoField(primary_key=True)
    username=models.CharField(('username'), max_length=40,unique=True)
    email=models.CharField(('email'), max_length=80,unique=True)
    is_verified=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    
    date_joined=models.DateTimeField(('date'),auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]
    objects=CustomUserManager()
    
    def __str__(self):
        return self.username
        


    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh':str(refresh.access_token),
            'access':str(refresh.access_token)
        }
        
        
        
    