from django.shortcuts import render,redirect, get_object_or_404
from ventasApp.models import Categoria,Cliente,Unidad,Producto,Venta,DetalleVenta
from django.contrib import messages
from django.db import transaction
from decimal import Decimal
from django.db.models import Q
from .forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from .utils import render_to_pdf
from django.http import HttpResponse
from .forms import CategoriaForm,ClienteForm,UnidadForm,ProductoForm
from .forms import CategoriaForm,ClienteForm,UnidadForm,ProductoForm,DetalleVentaForm,VentaForm
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import F
from .productos import Product
from .forms import CalculoFinancieroForm

# Create your views here.

#CATEGORIAS
@login_required
def listarcategoria(request):
    queryset = request.GET.get('search','').strip().lower()
    categoria = Categoria.objects.filter(estado=True)
    
    if queryset:
        categoria = Categoria.objects.filter(
            Q(descripcion__icontains=queryset),
            estado=True
        )
        
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
    return render(request, 'categoria_form.html', context)
@login_required
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

@login_required
def eliminarcategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.estado = False 
    categoria.save()
    messages.success(request, f'La categoría "{categoria.descripcion}" ha sido eliminada.')
    return redirect('listarcategoria')

#FIN CATEGORIAS

#UNIDADES
@login_required
def listar_unidades(request):
    queryset = request.GET.get("search",'').strip().lower()
    unidad = Unidad.objects.filter(estado=True)
    
    if queryset:
        unidad = Unidad.objects.filter(
            Q(descripcion__icontains=queryset),
            estado=True
        )
        
    context = {'unidad': unidad}
    return render(request, "listar_unidades.html", context)

@login_required
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
@login_required
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

@login_required
def eliminar_unidades(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    unidad.estado = False 
    unidad.save()
    messages.success(request, f'La Unidad "{unidad.descripcion}" ha sido eliminada.')
    return redirect('listar_unidades')
#FIN UNIDADES


#PRODUCTOS
@login_required
def listar_productos(request):
    search_query = request.GET.get('search', '').strip().lower()
    if search_query:
        productos = Producto.objects.filter(descripcion__icontains=search_query)
    else:
        productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

@login_required
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
@login_required
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
@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, f'El producto "{producto.descripcion}" ha sido eliminado.')
    return redirect('listar_productos')


#FIN PRODUCTOS


#CLIENTES
@login_required
def listar_clientes(request):
    search_query = request.GET.get('search', '').strip().lower()
    if search_query:
        clientes = Cliente.objects.filter(nombre__icontains=search_query)
    else:
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
@login_required
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

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, f'El cliente "{cliente.nombre} {cliente.apellidos}" ha sido eliminado.')
    return redirect('listar_clientes')
#FIN CLIENTES

@login_required
def reporte_pdf(request,id):
    
    venta =get_object_or_404(Venta, id=id)
    cliente = get_object_or_404(Cliente,id=venta.cliente_id)
    detalles = DetalleVenta.objects.filter(venta_id=id)
    productos = Producto.objects.all()
    
    lista = []
    re_cate = ""
    i=1
    
    for detalle in detalles:
        for prod in productos:
            if detalle.producto_id == prod.id:
                re_cate = get_object_or_404(Categoria,id=prod.categoria_id).descripcion
                nombre_producto = prod.descripcion
        pro = Product(i,nombre_producto,re_cate,detalle.cantidad,detalle.precio,detalle.cantidad*detalle.precio)
        lista.append(pro)
        i = i + 1
            
    context = {
        'venta' : venta,
        'cliente' : cliente,
        'productos':lista,
    }
    
    pdf = render_to_pdf('reporte.html', context)
    
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_categoria.pdf"'
        return response
    else:
        return HttpResponse("Error al generar el PDF", status=400)


#INICIO VENTAS
def listar_ventas(request):
    search_query = request.GET.get('search', '').strip().lower()
    if search_query:
        ventas = Venta.objects.filter(cliente__nombre__icontains=search_query)
    else:
        ventas = Venta.objects.all()

    context = {
        'ventas': ventas,
    }
    return render(request, 'listar_ventas.html', context)

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
                    print("POST data:", request.POST)
                    print("Productos IDs:", request.POST.getlist('id_producto[]'))
                    print("Cantidades:", request.POST.getlist('cantidad[]'))

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

                return JsonResponse({'success': True, 'redirect_url': reverse('listar_ventas')})
            except ValueError as e:
                return JsonResponse({'success': False, 'error': str(e)})
            except Exception as e:
                return JsonResponse({'success': False, 'error': f'Error al crear la venta: {str(e)}'})
        else:
            return JsonResponse({'success': False, 'error': 'Por favor, corrija los errores en el formulario.'})
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
                    precios = request.POST.getlist('precio[]')

                    if not productos_ids or not cantidades or not precios:
                        raise ValueError("No se han proporcionado productos, cantidades o precios.")
                    
                    for detalle in venta.detalles.all():
                        detalle.producto.stock += detalle.cantidad
                        detalle.producto.save()

                    venta.detalles.all().delete()
                    for producto_id, cantidad, precio in zip(productos_ids, cantidades, precios):
                        producto = get_object_or_404(Producto, id=producto_id)
                        cantidad = int(cantidad)
                        precio = Decimal(precio)

                        if producto.stock < cantidad:
                            raise ValueError(f"No hay suficiente stock para {producto.descripcion}. Stock disponible: {producto.stock}, solicitado: {cantidad}")

                        detalle = DetalleVenta(
                            venta=venta,
                            producto=producto,
                            precio=precio,
                            cantidad=cantidad
                        )
                        detalle.save()

                        producto.stock -= cantidad
                        producto.save()

                        total += precio * Decimal(cantidad)

                    venta.total = total
                    venta.save()

                return JsonResponse({'success': True, 'redirect_url': reverse('listar_ventas')})
            except ValueError as e:
                return JsonResponse({'success': False, 'error': str(e)})
            except Exception as e:
                return JsonResponse({'success': False, 'error': f'Error al actualizar la venta: {str(e)}'})
        else:
            return JsonResponse({'success': False, 'error': 'Por favor, corrija los errores en el formulario.'})
    else:
        venta_form = VentaForm(instance=venta)
        detalles = venta.detalles.all().select_related('producto')

    return render(request, 'editar_venta.html', {
        'venta_form': venta_form,
        'productos': productos,
        'clientes': clientes,
        'venta': venta,
        'detalles': detalles
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
def convertir_periodo(periodos, tipo_periodo, tipo_cap):
    conversion_frecuencias = {
        'dias': 1 / 360,     
        'meses': 1 / 12,     
        'años': 1,            
    }
    cap_años = {
        'diaria': 360,
        'semanal': 52,
        'mensual': 12,
        'trimestral': 4,
        'semestral': 2,
        'anual': 1,
    }
    periodos_en_anios = periodos * conversion_frecuencias[tipo_periodo]
    periodos_convertidos = periodos_en_anios * cap_años[tipo_cap]
    return periodos_convertidos


def convertir_tasa(tasa, frecuencia_origen, frecuencia_destino):
    periodos_por_frecuencia = {
        'diaria': 360,
        'semanal': 48,
        'mensual': 12,
        'trimestral': 4,
        'semestral': 2,
        'anual': 1
    }

    if frecuencia_origen == frecuencia_destino:
        return tasa
    
    if frecuencia_origen != 'anual':
        periodos_origen = periodos_por_frecuencia[frecuencia_origen]
        tasa_anual = (1 + tasa) ** periodos_origen - 1
    else:
        tasa_anual = tasa
    
    periodos_destino = periodos_por_frecuencia[frecuencia_destino]
    tasa_convertida = (1 + tasa_anual) ** (1 / periodos_destino) - 1
    
    return tasa_convertida

def calcular_factores(request):
    resultado = None
    if request.method == 'POST':
        form = CalculoFinancieroForm(request.POST)
        if form.is_valid():
            tipo_calculo = form.cleaned_data['tipo_calculo']
            capital = form.cleaned_data['capital']
            pago_periodico = form.cleaned_data['pago_periodico']
            tasa = form.cleaned_data['tasa'] / 100  
            periodos = form.cleaned_data['periodos']
            tipo_tasa = form.cleaned_data['tipo_tasa']
            tipo_capitalizacion = form.cleaned_data['tipo_capitalizacion']
            tipo_periodo = form.cleaned_data['tipo_periodo']

            tasa_convertida = convertir_tasa(tasa, tipo_tasa, tipo_capitalizacion)
            periodos_convertidos = convertir_periodo(periodos, tipo_periodo, tipo_capitalizacion)

            if tipo_calculo == 'frc':  
                resultado = calcular_factor_recuperacion(capital, tasa_convertida, periodos_convertidos)
            elif tipo_calculo == 'fas': 
                resultado = calcular_factor_actualizacion(pago_periodico, tasa_convertida, periodos_convertidos)

    else:
        form = CalculoFinancieroForm()

    return render(request, 'producto_form.html', {'form': form, 'resultado': resultado})


def calcular_factor_recuperacion(P, i, n):
    R = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return R


def calcular_factor_actualizacion(R, i, n):
    P = R * ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    return P
