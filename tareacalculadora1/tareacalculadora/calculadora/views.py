from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
# Create your views here.
def index(request):
    return render(request, 'index.html')


def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola '+ nombre)

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num = num1 * den2 + den1 * num2
    den = den1 * den2
    resultado = Fraccion(num,den)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num = num1 * den2 - den1 * num2
    den = den1 * den2
    resultado = Fraccion(num,den)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

def bienvenida(request):
    letrero = "Bienvenida"
    return HttpResponse(letrero)

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num = num1 * num2
    den = den1 * den2
    resultado = Fraccion(num,den)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    num = num1 * den2
    den = den1 * num2
    resultado = Fraccion(num,den)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")