
from django.urls import path
from block.views import post


urlpatterns = [

    path('', post),
] 
