from django.db import models
from django.contrib.auth.models import User

#class Citas(models.Model):
    # el modelo Citas hereda de models.Model, y cada campo del modelo (como id_citas, id_cliente, y fecha) es representado por una instancia de un tipo de campo específico de Django
    #id_citas = models.IntegerField(primary_key=True) #El parámetro primary_key=True se utiliza para indicar que id_citas es la clave primaria de la tabla.
    #id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    #fecha = models.DateField(null=True, default=None)

    # Definir la clave foránea
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente') 
    #En este modelo, ForeignKey se utiliza para definir la clave foránea (id_cliente)  indica que si se elimina un cliente, todas las citas asociadas a ese cliente también se eliminarán.

    #def __str__(self):
        #return f"Cita {self.id_citas} - Cliente: {self.id_cliente}"

    #class Meta:
        #db_table = 'citas'
    #la función __str__ proporciona una representación más legible al imprimir instancias de este modelo. 
    #La clase Meta se utiliza para configurar opciones adicionales, como el nombre de la tabla en la base de datos (db_table).

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=85, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=10, null=False, blank=False)
    empresa = models.CharField(max_length=55, null=False, blank=False)
    #AutoField se utiliza para representar la columna id_cliente con autoincremento. 
    #CharField se utilizan para los campos de texto (nombre, direccion, correo, telefono, y empresa).
    #EmailField se utiliza para el campo de correo electrónico.
    #null=False y blank=False se utilizan para indicar que estos campos no pueden ser nulos ni estar en blanco.

    def __str__(self):
        return self.nombre  

    class Meta:
        db_table = 'cliente'
    #la función __str__ proporciona una representación más legible al imprimir instancias de este modelo. 
    #La clase Meta se utiliza para configurar opciones adicionales, como el nombre de la tabla en la base de datos (db_table).
