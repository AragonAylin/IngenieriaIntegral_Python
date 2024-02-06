from django.urls import path
from .views import register_user
#views
from . import views
urlpatterns =[
    path('',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('register/', register_user, name='register_user')
]