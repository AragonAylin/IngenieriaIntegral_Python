from django.urls import path
from . import views
urlpatterns =[
    path('somos',views.somos, name='somos')
]