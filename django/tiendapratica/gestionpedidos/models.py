from django.db import models

# Create your models here.
class proyecto(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField()
    link=models.URLField(None)
    web=models.BooleanField(None)
    ciencia_de_datos=models.BooleanField(None)
    analisis_de_datos=models.BooleanField(None)
    tranding=models.BooleanField(None)
    