from django.shortcuts import render,redirect
from ventasApp.models import Categoria 
from django.db.models import Q
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from .utils import render_to_pdf
from django.http import HttpResponse

# Create your views here.
@login_required
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
@login_required
def agregarcategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm()
        
    context = {'form': form}
    return render(request, "agregar.html", context)
@login_required
def editarcategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {"form": form}
    return render(request, "editar.html", context)

@login_required
def eliminarcategoria(request,id):
    categoria=Categoria.objects.get(id=id) 
    categoria.estado=False
    categoria.save()
    return redirect("listarcategoria")

def reporte_pdf(request):
    # Suponiendo que tienes una lista de categorías en tu contexto
    categorias = Categoria.objects.all()
    
    context = {
        'categoria': categorias,
    }
    
    pdf = render_to_pdf('listarcategoria.html', context)
    
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_categoria.pdf"'
        return response
    else:
        return HttpResponse("Error al generar el PDF", status=400)


