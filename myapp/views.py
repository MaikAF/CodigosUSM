from django.shortcuts import render
from .models import Comunicado, Entidad
def index(request):
    title = "Inicio"

    data = {
        "title": title,
        "comunicados" : Comunicado.objects.all(),
        "entidades" : Entidad.objects.all(),
    }

    return render(request,'myapp/index.html', data)

def nuevo(request):
    filtro = request.GET.get('Depto')
    coms =  Comunicado.objects.all().order_by('-fecha_publicacion')
    title = "Inicio"
    entity = None
    if filtro!='Departamentos' and filtro!=None:
        entity = Entidad.objects.filter(nombre=filtro).first() 
        if entity:
            coms = Comunicado.objects.filter(entidad=entity).order_by('-fecha_publicacion')
        
    data = {
        "title": title,
        "comunicados" : coms,
        "entidades" : Entidad.objects.all(),
        "logoEnt": entity.logo if entity and entity.logo else None,
        }
    return render(request,'myapp/index.html', data)