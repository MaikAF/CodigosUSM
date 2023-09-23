from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = "home"
    page = "<html>"
    page += "<head>"
    page += "<title>" + title + "</title>"
    page += "</head>"
    page += "<body>"
    page += "<h1>" + title + "</h1>"
    page += "</body>"
    page += "</html>"
    return HttpResponse(page)


def carreras(request):
    title= "Carreras"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+ title +"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+ title +"</h1>"
    page+= "</body>"
    page+= "<html>"
    return HttpResponse(page)

def docentes(request):
    title= "docentes"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+ title +"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+ title +"</h1>"
    page+= "</body>"
    page+= "<html>"
    return HttpResponse(page)
