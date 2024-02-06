#Estas son importaciones necesarias para manejar mensajes, renderizar plantillas y gestionar la autenticacion de usuarios en Django.
from django.contrib import messages
from django.shortcuts import render, redirect # Importa la funcion render, render se utiliza para renderizar una plantilla de django con un contexto especifico y devolver el resultado como una respuesta HTTP.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Define una vista para el inicio de sesión de usuario.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Esta parte verifica si el formulario se envia utilizando el metodo POST.

        # Autenticar al usuario 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es autenticado,  si la autenticacion es exitosa, se inicia sesion para el usuario.
            login(request, user)
            if user.is_staff and user.is_superuser:
                # El usuario es miembro del grupo "Administrator"
                print("Redireccionando a 'vistaadmin' para administrador")
                return redirect('admin1')
            else:
                #El usuario no es administrador, redirigir a la página de clientes
                print("Redireccionando a 'vistausuario' para no administrador")
                return redirect('usuario')
        else:
            #El usuario no es autenticado, mostrar un mensaje de error
            messages.error(request, 'El nombre de usuario o contraseña no son correctos.')
            return redirect('login')
    else:
        return render(request, 'login.html')
        #Si el metodo de solicitud no es POST o la autenticacion falla, renderiza la plantilla de inicio de sesion.

def register_user(request):
    #Esta parte verifica si el formulario se envia utilizando el metodo POST.
    if request.method == 'POST':
        #Recupera el nombre de usuario y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            #Crear un nuevo usuario
            user = User.objects.create_user(username=username, password=password)
            print(f"Usuario {username} creado exitosamente.")

            #Autenticar al usuario recién creado
            user = authenticate(request, username=username, password=password)
            login(request, user)


        else:
            print(f"El usuario {username} ya existe.")

    return render(request, 'register_user.html')

def logout_user(request):
    #Cerrar sesión del usuario
    logout(request)
    return redirect('login')
