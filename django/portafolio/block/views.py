from django.shortcuts import render
from block.models import post
# Create your views here.

def render_post (request):
    
    posts= post.objects.all()
    
    return render( request, 'post.html', {"post":posts})