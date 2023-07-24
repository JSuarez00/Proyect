from django.db import models

# Create your models here.

class post(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=2000)
    imagen=models.ImageField(upload_to='miportafolio/media/images')
    link=models.URLField(None)
    web=models.BooleanField(None)
    ciencia_de_datos=models.BooleanField(None)
    analisis_de_datos=models.BooleanField(None)
    trading=models.BooleanField(None)
    
    def __str__(self):
        
        return "post: " + self.nombre
