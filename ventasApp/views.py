from django.shortcuts import render,redirect, get_object_or_404
from ventasApp.models import Categoria 
from django.contrib import messages
from django.db.models import Q
from .forms import CategoriaForm
# Create your views here.
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
