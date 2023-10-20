from django.db import models

TIPO_CHOICES = [
    ('S', 'Suspencion de actividades'),
    ('C', 'Suspencion de clase'),
    ('I', 'Informacion'),
]


class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=50)
    detalle= models.CharField(max_length=100)
    detalle_corto= models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    entidad=models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_ultima_publicacion = models.DateTimeField(null=True, blank=True)
    #publicado_por =

    def __str__(self) -> str:
        return self.titulo
    
