from django.urls import path,include 
from ventasApp.views import listarcategoria,agregarcategoria,editarcategoria,eliminarcategoria,listar_clientes,crear_cliente,editar_cliente,eliminar_cliente
from django.contrib.auth import views
urlpatterns = [ 
    path('listacategoria/',listarcategoria,name="listarcategoria"), 
    path('agregarcategoria/',agregarcategoria ,name="agregarcategoria"),
    path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"),
    path('eliminarcategoria/<int:id>/',eliminarcategoria,name="eliminarcategoria"),  
    
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
    ]


