from django.shortcuts import render
from .models import Pariente
from django.http import HttpResponse
from django.template import Template, Context


# Create your views here.


def crearPariente(request):
    persona_a = Pariente(nombre = "Arturo", apellido ="Wetz", edad = 73)
    persona_b = Pariente(nombre = "Lia",apellido = "Wetz", edad = 73)
    persona_c = Pariente(nombre = "Ignacio", apellido ="Wetz",edad = 44)
    familiares = {"lista_de_familiares": [persona_a, persona_b, persona_c]}
    archivo = open('C:\CH\PrimerMVP\primeraApp\Templates\Template1.html')
    template = Template(archivo.read())
    contexto = Context(familiares)
    documento = template.render(contexto)
    return HttpResponse(documento)

def inicio(request):
    return HttpResponse("estoy en Inicio!")