from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def home(request):
    return HttpResponse('bienvenidos...')

def newMember(resp):
    if resp.method == 'POST':
        return HttpResponse('agregar nuevo usuario')
    else: 
        return HttpResponseNotAllowed('POST', 'metodo no permitido')
    
def readMember(respuesta):
    if respuesta.method == "GET":
        return HttpResponse('informacion de usuario')
    else:
        return HttpResponseNotAllowed("GET","metodo no permitido")
