from django.shortcuts import render
from miportafolio.models import proyecto
# Create your views here.


def home(resquest):
    project=proyecto.objects(all)
    
    return render(resquest ,"template.html" ,{proyecto:project})
