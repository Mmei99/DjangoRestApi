from django.db import models
from django.contrib.auth import get_user_model
from .models import User,Movie








class Rental(models.Model):
    rental_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def create_rental(self,rental_id,user_id,created_at):
        if not rental_id:
            raise ValueError(_('Please enter a name'))
        if not category:
            raise ValueError(_('Please enter a category'))
        if not description:
            raise ValueError(_('Please enter a descriptio'))
        
        

        
        new_movie=self.model(name=name,category=category,description=description)

        

        new_movie.save()

        return new_movie
    
    def __str__(self):
        return self.rental_id + ' ' + self.user_id + ' ' + self.created_at
    
    
    
        
        
    
    
    

