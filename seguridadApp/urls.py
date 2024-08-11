from django.urls import path
from seguridadApp.views import homePage, salir,ingresar_login,register
from django.contrib.auth import views

urlpatterns = [
    path('', ingresar_login, name='login'),
    path('register/', register, name='register'),
    path('home/', homePage, name='homePage'),
    path('logout/',salir,name="logout"), 
]
