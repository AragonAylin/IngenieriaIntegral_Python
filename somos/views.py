from django.shortcuts import render # Importa la funcion render, render se utiliza para renderizar una plantilla de django con un contexto especifico y devolver el resultado como una respuesta HTTP.

# Create your views here.
# Vistas para la paguina somos.
# Estas funciones representan diferentes paginas en la appweb.

def somos(request):
    return render(request, 'somos.html')