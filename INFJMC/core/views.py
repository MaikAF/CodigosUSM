from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = "Inicio"
    data = {
        "title": title,
    }
    return render(request,'core/index.html', data)

def carreras(request):
    title = "carreras"
    return HttpResponse(title)

def docentes(request):
    title = "request"
    return HttpResponse(title)
