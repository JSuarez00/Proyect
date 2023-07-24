from django.shortcuts import render
from miportafolio.models import proyecto
# Create your views here.


def home(resquest):
    projects=proyecto.objects.all()
    
    return render(resquest ,"index.html", {"projects":projects} )
