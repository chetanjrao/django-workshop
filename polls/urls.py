from django.urls import path
from .views import tw_login, tweets

urlpatterns = [
   path('', tweets, name='home'),
   path('login/', tw_login, name='login')
]