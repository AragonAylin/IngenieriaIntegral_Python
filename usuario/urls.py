# Este codigo define las URL de tu aplicacion.
from django.urls import path
from . import views
urlpatterns =[
    path('', views.usuario, name='usuario'),
    path('bitacoraU/', views.bitacoraU, name='bitacoraU'),
    path('descargasU/', views.descargasU, name='descargasU'),
    path('proximascitasU/', views.proximascitasU, name='proximascitasU'),
]