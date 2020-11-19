from django.urls import path
from .views import submit_tweet, tw_login, tweets

urlpatterns = [
   path('', tweets, name='home'),
   path('login/', tw_login, name='login'),
   path('tweet/', submit_tweet, name='tweet')
]