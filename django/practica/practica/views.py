from django.http import HttpResponse

def hola(resquest): # cada funcion se reconoce como una vista
    return HttpResponse("hola mundo mi primera pag web  en django ")

def despedida(resquest):
    return HttpResponse("esta es mi pag de despedida para la pagina django de JASZ")