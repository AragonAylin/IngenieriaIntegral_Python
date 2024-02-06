from django.shortcuts import render# Importa la funcion render, render se utiliza para renderizar una plantilla de django con un contexto especifico y devolver el resultado como una respuesta HTTP.

# Create your views here.
# Vistas para la paguina core index.
# Estas funciones representan diferentes paginas en la appweb.
def index(request):
    return render(request, 'index.html')