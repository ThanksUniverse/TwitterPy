from django.urls import path  
from .views import create_tweet 

urlpatterns = [  
    path('create/', create_tweet, name='create_tweet')
]