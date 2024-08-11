from django import forms 
from django.forms import fields 
from .models import Categoria, Cliente, Unidad,Producto,Venta,DetalleVenta

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'placeholder': 'Ingrese una descripción'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'sr-only',
                'x-model': 'checkboxToggle'
            })
        }
        
class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'placeholder': 'Ingrese una descripción'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'sr-only',
                'x-model': 'checkboxToggle'
            })
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'documento', 'email', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'}),
            'apellidos': forms.TextInput(attrs={'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'}),
            'documento': forms.TextInput(attrs={'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'}),
            'email': forms.EmailInput(attrs={'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'}),
            'direccion': forms.Textarea(attrs={'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary', 'rows': 3}),
        }
 
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'categoria', 'unidad', 'stock', 'precio']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
            }),
            'categoria': forms.Select(attrs={
                'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'x-data': '{ isOptionSelected: false }',
                '@change': 'isOptionSelected = true',
                ':class': 'isOptionSelected && "text-black dark:text-white"'
            }),
            'unidad': forms.Select(attrs={
                'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'x-data': '{ isOptionSelected: false }',
                '@change': 'isOptionSelected = true',
                ':class': 'isOptionSelected && "text-black dark:text-white"'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
            }),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'fecha_venta', 'documento', 'total']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'x-data': '{ isOptionSelected: false }',
                '@change': 'isOptionSelected = true',
                ':class': 'isOptionSelected && "text-black dark:text-white"'
            }),
            'fecha_venta': forms.DateInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'type': 'date'
            }),
            'documento': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'placeholder': 'DNI del cliente',
                'readonly':'readonly'
            }),
            'total': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'step': '0.01',
                'readonly': 'readonly'
            }),
            'subtotal': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'step': '0.01',
                'readonly': 'readonly'
            }),
            'igv': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'step': '0.01',
                'readonly': 'readonly'
            }),
        }
        
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'precio', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'x-data': '{ isOptionSelected: false }',
                '@change': 'isOptionSelected = true',
                ':class': 'isOptionSelected && "text-black dark:text-white"'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'step': '0.01'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
                'min': '1'
            }),
        }