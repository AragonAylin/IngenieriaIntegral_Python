from django.shortcuts import render #funciones de django
from .forms import ClienteForm #traer el formulario de cliente de la app
from django.contrib import messages#se utiliza para mostrar mensajes
from .models import Cliente #importa el modelo de cliente de la app
from django.shortcuts import render, get_object_or_404, redirect  #indica que va a recuperar un argumento y va a devolver un httpresponse
from django.http import JsonResponse #Importa la clase JsonResponse desde el módulo django.http. JsonResponse es una clase que facilita la creacion de respuestas HTTP en formato JSON
from django.views.decorators.csrf import csrf_exempt #se desactiva la verificación CSRF para esa vista en particular. Esto puede ser útil en situaciones donde necesitas permitir solicitudes POST sin el token CSRF

# Create your views here.
# Vistas para la paguina admin.
# Estas funciones representan diferentes paginas en la appweb.
def admin1(request):
    return render(request, 'admin.html')

def bitacorasadmin(request):
    return render(request, 'bitacorasadmin.html')

def descargasadmin(request):
    return render(request, 'descargasadmin.html')

def listaclientes(request):
    return render(request, 'listaclientes.html')

def pcitasadmin(request):
    return render(request, 'pcitasadmin.html')


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Vincula el formulario con los datos POST
        if form.is_valid():
            form.save() # Guarda los datos en la base de datos
            messages.success(request, 'Cliente creado con exito.') # Muestra un mensaje de éxito
            return redirect('listar') # Redirige a la página de listado de los clientes
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)  # Agrega mensajes de error detallados
    else:
        form = ClienteForm()  # Crea un objeto vacío 
    return render(request, 'listaclientes.html', {'form': form})# Renderiza la plantilla HTML con el formulario

#funcion para mostrar la lista de los clientes
def listar_cliente(request): #hacemos la solicitud al servidor con la funcion request
    clientes = Cliente.objects.all() #mostramos los clientes almacenaso en la base de datos
    return render (request, "listaclientes.html", {"clientes":clientes}) #respuesta del servidor en la pagina listaclientes

#funcion para actualizar o modificar los datos del cliente
def update_cliente(request, id_cliente): #obtener los datos del cliente mediante el id
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = ClienteForm(request.POST, instance=cliente) #se crea el formulario para la validacion
        if form.is_valid():
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar') #se regresa al la pagina donde estan los clientes
        else: #Else se ejecuta si la condicion en el bloque "if" no se cumple.
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else: #Else se ejecuta si la condicion en el bloque "if" no se cumple.
        data = { #Recupera datos del objeto cliente
            'nombre':cliente.nombre,
            'direccion':cliente.direccion,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
            'empresa':cliente.empresa,
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_cliente(request, id_cliente):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente) 
            cliente.delete()
            return JsonResponse({'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)#error en el servidor
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=403)
#get_object_or_404 devuelve un objeto o genera una excepcion