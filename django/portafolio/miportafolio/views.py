from django.shortcuts import render
from miportafolio.models import proyecto
# Create your views here.


def home(request):
    projects=proyecto.objects.all()
    
    return render(request ,"index.html", {"projects":projects} )
