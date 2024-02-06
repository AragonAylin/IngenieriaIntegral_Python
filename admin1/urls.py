from django.urls import path
from django.contrib.auth.decorators import login_required 
from . import views
urlpatterns =[
    path('admin1',views.admin1, name='admin1'),
    path('bitacorasadmin/',views.bitacorasadmin, name='bitacorasadmin'),
    path('descargasadmin/',views.descargasadmin, name='descargasadmin'),
    path('listar/',views.listaclientes, name='listar'),
    path('pcitasadmin/',views.pcitasadmin, name='pcitasadmin'),
    path('create',views.create_cliente, name='create'),
    path('listar', login_required (views.listar_cliente), name='listar'),
    path('editar_cliente/<int:id_cliente>', login_required (views.update_cliente), name='editar_cliente'),
    path('eliminar/<int:id_cliente>', views.delete_cliente, name='eliminar_cliente'),
] 
