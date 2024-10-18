from django.shortcuts import render,redirect, get_object_or_404
from ventasApp.models import Categoria,Cliente,Unidad,Producto
from django.contrib import messages
from django.db.models import Q
<<<<<<< Updated upstream
from .forms import CategoriaForm,ClienteForm,UnidadForm,ProductoForm
=======
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from .utils import render_to_pdf
from django.http import HttpResponse
from .forms import CategoriaForm,ClienteForm,ProductoForm
from .forms import CategoriaForm,ClienteForm,ProductoForm,DetalleVentaForm,VentaForm
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import F
from .productos import Product
>>>>>>> Stashed changes
# Create your views here.

#CATEGORIAS
def listarcategoria(request):
    queryset = request.GET.get("buscar")
    categoria = Categoria.objects.filter(estado=True)
    
    if queryset:
        categoria = Categoria.objects.filter(
            Q(descripcion__icontains=queryset),
            estado=True
        ).distinct()
        
    context = {'categoria': categoria}
    return render(request, "listarCategoria2.html", context)


def agregarcategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm()

    context = {'form': form}
    return render(request, 'categoria_form.html', context)

def editarcategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listarcategoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})


def eliminarcategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.estado = False 
    categoria.save()
    messages.success(request, f'La categoría "{categoria.descripcion}" ha sido eliminada.')
    return redirect('listarcategoria')

#FIN CATEGORIAS

#UNIDADES
def listar_unidades(request):
<<<<<<< Updated upstream
    queryset = request.GET.get("buscar")
    unidad = Unidad.objects.filter(estado=True)
    
    if queryset:
        unidad = Unidad.objects.filter(
            Q(descripcion__icontains=queryset),
            estado=True
        ).distinct()
        
    context = {'unidad': unidad}
    return render(request, "listar_unidades.html", context)


def agregar_unidades(request):
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_unidades")
    else:
        form = UnidadForm()

    context = {'form': form}
    return render(request, 'unidad_form.html', context)

def editar_unidades(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    if request.method == 'POST':
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades')
    else:
        form = UnidadForm(instance=unidad)
    return render(request, 'editar_unidades.html', {'form': form})


def eliminar_unidades(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    unidad.estado = False 
    unidad.save()
    messages.success(request, f'La Unidad "{unidad.descripcion}" ha sido eliminada.')
    return redirect('listar_unidades')
#FIN UNIDADES


=======
    unidades = Unidad.objects.all() 
    context = {'unidad': unidades}  
    return render(request, "listar_unidades.html", context)

>>>>>>> Stashed changes
#PRODUCTOS
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
        form.fields['categoria'].queryset = Categoria.objects.filter(estado=True)
        form.fields['unidad'].queryset = Unidad.objects.filter(estado=True)

    return render(request, 'producto_form.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('listar_productos')
        else:
            print(form.errors)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, f'El producto "{producto.descripcion}" ha sido eliminado.')
    return redirect('listar_productos')


#FIN PRODUCTOS


#CLIENTES
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('listar_clientes')
        else:
            print(form.errors)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, f'El cliente "{cliente.nombre} {cliente.apellidos}" ha sido eliminado.')
    return redirect('listar_clientes')
#FIN CLIENTES