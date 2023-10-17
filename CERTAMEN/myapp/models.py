from django.db import models

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.nombre
    
"""
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=50)
    detalle= models.CharField(max_length=100)
    detalle_corto= models.CharField(max_length=100)
    entidad=Entidad()
    visible= bool()
    fecha_publicacion = date()
"""
    def __str__(self) -> str:
        return self.nombre
    
