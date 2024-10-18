from django.urls import path,include 
from ventasApp.views import (
    listarcategoria, agregarcategoria, editarcategoria, eliminarcategoria,
    listar_clientes, crear_cliente, editar_cliente, eliminar_cliente,
<<<<<<< Updated upstream
    listar_unidades, agregar_unidades, eliminar_unidades, editar_unidades,
    listar_productos, crear_producto, editar_producto, eliminar_producto
=======
    listar_unidades,
    listar_productos, crear_producto, editar_producto, eliminar_producto,
    listar_ventas, crear_venta, editar_venta, eliminar_venta, get_cliente_documento,reporte_pdf 
>>>>>>> Stashed changes
)
from django.contrib.auth import views
urlpatterns = [ 
    path('listacategoria/',listarcategoria,name="listarcategoria"), 
    path('agregarcategoria/',agregarcategoria ,name="agregarcategoria"),
    path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"),
    path('eliminarcategoria/<int:id>/',eliminarcategoria,name="eliminarcategoria"), 
    
    path('listar_unidades/',listar_unidades,name="listar_unidades"), 

    
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
    
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
    
    ]


