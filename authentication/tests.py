from rest_framework.test import APITestCase
from django.urls import reverse,resolve
from . import views as views
from rest_framework import generics,status
from Movies import views
from .serializers import UserCreationSerializer
from rest_framework.response import Response
from .models import User

class TestSetUp(APITestCase):
    
   def setUp(self):
       self.register_url=reverse("sign_up")
       self.login_url=reverse("login")
       
       self.user_data={"username":"user35",
                  "email":"user35@gmail.com",
                  "password":"user35"
                  }
       self.user_data_login={"email":"user20@gmail.com",
                  "password":"user20"
                  }
       
       
       return super().setUp()
   
   def tearDown(self):
       return super().tearDown()
       
   
           
class TestViews(TestSetUp):
    
    def test_user_cannot_register_with_no_data(self):
       res=self.client.post(self.register_url)
       
       self.assertEqual(res.status_code,400)

    def test_user_can_register_with_data(self):
        res=self.client.post(self.register_url,self.user_data)
       
        self.assertEqual(res.status_code,201)
        
    
        
    def test_Movies_List(self):
        url=reverse("Movies_List")
        response=self.client.get(url)
        print(resolve(url).func.view_class,views.Movies_List)
        self.assertEqual(resolve(url).func.view_class,views.Movies_List)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        
    
       
       
       
   
