from django.db import models
from django.contrib.auth import get_user_model
   
   
   
User=get_user_model()



class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    category=models.CharField(max_length=40)
    description=models.CharField(max_length=200)
    
    REQUIRED_FIELDS=['username','category','description']
    
    
    def create_movie(self,name,category,description):
        if not name:
            raise ValueError(_('Please enter a name'))
        if not category:
            raise ValueError(_('Please enter a category'))
        if not description:
            raise ValueError(_('Please enter a descriptio'))
        
        

        
        new_movie=self.model(name=name,category=category,description=description)

        

        new_movie.save()

        return new_movie
    
    def __str__(self):
        return self.name + ' ' + self.description + ' ' + self.category 
    
    
    



