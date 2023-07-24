from django.http import HttpResponse
import datetime

from django.shortcuts import render

#from django.template import Template, Context

def hola(resquest):
    # cada funcion se reconoce como una vista
    name="Jasz"
    
    return render(resquest,'template.html', {"name":name})


def despedida(resquest):

    return HttpResponse("esta es mi pag de despedida para la pagina django de JASZ")


def calcula_edad(resquest,year):

    years= 1997

    periodo= year - years 

    edad=26

    return HttpResponse("<H1>mi edad es %s en %s tendre %s</H1>" %(edad, year,periodo))


def fecha(resquest):

    fecha2 = datetime.datetime.today()

    fecha3='esta es la fecha actual: ',fecha2

    return HttpResponse(fecha3)