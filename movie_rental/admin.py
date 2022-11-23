from django.contrib import admin
from .models import User,Movie_Rental
# Register your models here.

@admin.register(Movie_Rental)
class Movie_Rental(admin.ModelAdmin):
    list_display=['rental_id','movie_id']
    
    
    
    def __str__(self):
        return self.rental_id + ' ' + self.movie_id 
    