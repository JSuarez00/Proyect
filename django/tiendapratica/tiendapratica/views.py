from django.shortcuts import render
from django.template import Template,context
from django.http import HttpResponse
from gestionpedidos.models import proyecto

# Create your views here.

def proyecto1(resquest):
    Titulo=proyecto.nombre
    
    
    return render(resquest,"template.html")