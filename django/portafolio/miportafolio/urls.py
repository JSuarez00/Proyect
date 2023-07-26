
from django.urls import path
from miportafolio import views

urlpatterns = [
    path('', views.home, name= 'home'),
   
] 
