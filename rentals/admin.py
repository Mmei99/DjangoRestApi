from django.contrib import admin
from .models import Rental



@admin.register(Rental)
class Rental(admin.ModelAdmin):
    list_display=['user_id','movie_id']