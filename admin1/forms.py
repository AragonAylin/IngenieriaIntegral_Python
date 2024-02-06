from django import forms #Importa el  forms de Django que proporciona clases y funciones 
from django.forms import ModelForm #Importa clases ModelForm es una clase base especializada para la creación de formularios basados en modelos.
from .models import Cliente #Importa el modelo Cliente el modelo Cliente tiene que estar definido en el archivo models.py

class ClienteForm(forms.ModelForm): #indica que ClienteForm será un formulario basado en un modelo de Django.
    class Meta: #clase se utiliza para proporcionar metadatos sobre el formulario.
        model = Cliente #especifica el modelo asociado al formulario
        fields = ["nombre","direccion","correo","telefono","empresa",] 
        #Indica los campos del modelo Cliente que deben incluirse en el formulario campos que el usuario podra completar al utilizar el formulario.