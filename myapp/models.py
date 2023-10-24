from django.db import models
from django.contrib.auth.models import User


TIPO_CHOICES = [
    ('S', 'Suspencion de actividades'),
    ('C', 'Suspencion de clase'),
    ('I', 'Informacion'),
]


class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to='fotos')
    administrador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"
    

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=50)
    detalle= models.CharField(max_length=100)
    detalle_corto= models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    entidad=models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_ultima_publicacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    publicado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comunicados_publicados')
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comunicados_modificados')


    def __str__(self) -> str:
        return self.titulo
    
