from django.shortcuts import render,redirect, get_object_or_404
from ventasApp.models import Categoria,Cliente,Unidad,Producto,Venta,DetalleVenta
from django.contrib import messages
from django.db import transaction
from decimal import Decimal
from django.db.models import Q
from .forms import CategoriaForm,ClienteForm,UnidadForm,ProductoForm,DetalleVentaForm,VentaForm
from django.http import JsonResponse
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


#INICIO VENTAS
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'listar_ventas.html', {'ventas': ventas})

@transaction.atomic
def crear_venta(request):
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            try:
                with transaction.atomic():
                    venta = venta_form.save(commit=False)
                    
                    total = Decimal('0.00')
                    productos_ids = request.POST.getlist('id_producto[]')
                    cantidades = request.POST.getlist('cantidad[]')

                    if not productos_ids or not cantidades:
                        raise ValueError("No se han proporcionado productos o cantidades.")

                    for producto_id, cantidad in zip(productos_ids, cantidades):
                        producto = get_object_or_404(Producto, id=producto_id)
                        
                        stock_disponible = int(producto.stock or 0) 
                        cantidad_solicitada = int(cantidad)
                        
                        if stock_disponible < cantidad_solicitada:
                            raise ValueError(f"No hay suficiente stock para {producto.descripcion}. Stock disponible: {stock_disponible}, solicitado: {cantidad_solicitada}")
                        
                        total += producto.precio * Decimal(cantidad_solicitada)
                    total_con_igv = total * Decimal('1.18')
                    venta.total = total_con_igv
                    venta.save()

                    # crea detalles de la venta
                    for producto_id, cantidad in zip(productos_ids, cantidades):
                        producto = get_object_or_404(Producto, id=producto_id)
                        detalle = DetalleVenta(
                            venta=venta,
                            producto=producto,
                            precio=producto.precio,
                            cantidad=int(cantidad) 
                        )
                        detalle.save()
                        
                        #actualiza stock
                        producto.stock = int(producto.stock or 0) - int(cantidad)
                        producto.save()

                messages.success(request, 'Venta creada exitosamente.')
                return redirect('listar_ventas')
            except ValueError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, f'Error al crear la venta: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        venta_form = VentaForm()

    return render(request, 'venta_form.html', {
        'venta_form': venta_form,
        'productos': productos,
        'clientes': clientes
    })

    
@transaction.atomic
def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        venta_form = VentaForm(request.POST, instance=venta)
        if venta_form.is_valid():
            try:
                with transaction.atomic():
                    venta = venta_form.save(commit=False)
                    
                    total = Decimal('0.00')
                    productos_ids = request.POST.getlist('id_producto[]')
                    cantidades = request.POST.getlist('cantidad[]')

                    if not productos_ids or not cantidades:
                        raise ValueError("No se han proporcionado productos o cantidades.")

                    for detalle in venta.detalleventa_set.all():
                        detalle.producto.stock += detalle.cantidad
                        detalle.producto.save()

                    venta.detalleventa_set.all().delete()

                    for producto_id, cantidad in zip(productos_ids, cantidades):
                        producto = get_object_or_404(Producto, id=producto_id)
                        
                        stock_disponible = int(producto.stock or 0) 
                        cantidad_solicitada = int(cantidad)
                        
                        if stock_disponible < cantidad_solicitada:
                            raise ValueError(f"No hay suficiente stock para {producto.descripcion}. Stock disponible: {stock_disponible}, solicitado: {cantidad_solicitada}")
                        
                        total += producto.precio * Decimal(cantidad_solicitada)
                    
                    total_con_igv = total * Decimal('1.18')
                    venta.total = total_con_igv
                    venta.save()

                    for producto_id, cantidad in zip(productos_ids, cantidades):
                        producto = get_object_or_404(Producto, id=producto_id)
                        detalle = DetalleVenta(
                            venta=venta,
                            producto=producto,
                            precio=producto.precio,
                            cantidad=int(cantidad)
                        )
                        detalle.save()
                        
                        producto.stock = int(producto.stock or 0) - int(cantidad)
                        producto.save()

                messages.success(request, 'Venta actualizada exitosamente.')
                return redirect('listar_ventas')
            except ValueError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, f'Error al actualizar la venta: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        venta_form = VentaForm(instance=venta)

    return render(request, 'venta_form.html', {
        'venta_form': venta_form,
        'productos': productos,
        'clientes': clientes,
        'venta': venta
    })

@transaction.atomic
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)

    if request.method == 'POST':
        try:
            detalles = venta.detalles.all()

            if detalles.exists():
                for detalle in detalles:
                    producto = detalle.producto
                    producto.stock += detalle.cantidad
                    producto.save()
                
                detalles.delete()

            venta.delete()

            messages.success(request, 'Venta eliminada exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al eliminar la venta: {str(e)}')
        return redirect('listar_ventas')

    return redirect('listar_ventas')

    
def get_cliente_documento(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        return JsonResponse({'documento': cliente.documento})
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

#FIN VENTAS