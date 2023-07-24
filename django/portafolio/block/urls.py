
from django.urls import path
from block.views import render_post


urlpatterns = [

    path('', render_post),
] 
