from django.shortcuts import render,redirect, get_object_or_404
from ventasApp.models import Categoria,Cliente,Unidad
from django.contrib import messages
from django.db.models import Q
from .forms import CategoriaForm,ClienteForm,UnidadForm
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
    categoria.estado = False  # Asumiendo que False representa el estado "eliminado"
    categoria.save()
    messages.success(request, f'La categoría "{categoria.descripcion}" ha sido eliminada.')
    return redirect('listarcategoria')

#FIN CATEGORIAS

#UNIDADES
def listar_unidades(request):
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
        form = UnidadForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_unidades')
    else:
        form = UnidadForm(instance=unidad)
    return render(request, 'editar_unidades.html', {'form': form})


def eliminar_unidades(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    unidad.estado = False  # Asumiendo que False representa el estado "eliminado"
    unidad.save()
    messages.success(request, f'La categoría "{unidad.descripcion}" ha sido eliminada.')
    return redirect('listarcategoria')
#FIN UNIDADES



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
    return render(request, 'cli ente_form.html', {'form': form})

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