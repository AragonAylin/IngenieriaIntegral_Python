from django.shortcuts import render # Importa la funcion render, render se utiliza para renderizar una plantilla de django con un contexto especifico y devolver el resultado como una respuesta HTTP.

# Create your views here.
# Vistas para la paguina usuario.
# Estas funciones representan diferentes paginas en la appweb.

def usuario(request):
    return render(request, 'usuario.html')

def bitacoraU(request):
    return render(request, 'bitacoraU.html')

def descargasU(request):
    return render(request, 'descargasU.html')

def proximascitasU(request):
    return render(request, 'proximascitasU.html')