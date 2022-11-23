from django.urls import path
from. import views


urlpatterns = [
    path('',views.Movies_List().as_view(),name='Movies_List'),
    path('<str:category>',views.Movies_get_by_category().as_view(),name='Movies_By_Category'),
    path('details/<str:name>',views.MovieDetailView().as_view(),name='Movies_Detail'),
   
]
