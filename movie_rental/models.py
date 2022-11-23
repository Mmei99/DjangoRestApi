from django.db import models
from django.contrib.auth import get_user_model
from .models import Rental,Movie


User=get_user_model()
class Movie_Rental(models.Model):
    rental_id=models.ForeignKey(Rental,on_delete=models.CASCADE)
    movie_id=models.ForeignKey(Movie,on_delete=models.CASCADE)
    REQUIRED_FIELDS=['rental_id','movie_id']
    
    def create_rental(self,rental_id,user_id,created_at):
        if not rental_id:
            raise ValueError(_('Please enter a name'))
        if not category:
            raise ValueError(_('Please enter a category'))
        if not description:
            raise ValueError(_('Please enter a descriptio'))