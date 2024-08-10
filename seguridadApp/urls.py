from django.urls import path
from seguridadApp.views import acceder, homePage, salir
from django.contrib.auth import views

urlpatterns = [
    path('', acceder, name='login'),
    path('home/', homePage, name='homePage'),
    path('logout/',salir,name="logout"), 
]
