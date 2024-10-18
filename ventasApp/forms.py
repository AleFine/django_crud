from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields 
from .models import Categoria, Cliente, Unidad,Producto,Venta,DetalleVenta,FactorCapitalizacion

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
  
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu nombre de usuario'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu contraseña'
        })
    )

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu correo electrónico'
        })
    )
    
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu usuario'
        })
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu contraseña'
        })
    )
    
    password2 = forms.CharField(
        label='Repite tu contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa nuevamente tu contraseña'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
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
        
TIPO_CALCULO_CHOICES = [
    ('frc', 'Factor de Recuperación de Capital'),
    ('fas', 'Factor de Actualización de la Serie'),
]

FRECUENCIA_CHOICES = [
    ('diaria', 'Diaria'),
    ('semanal', 'Semanal'),
    ('mensual', 'Mensual'),
    ('trimestral', 'Trimestral'),
    ('semestral', 'Semestral'),
    ('anual', 'Anual'),
]

TIPO_PERIODO_CHOICES = [
    ('dias', 'Días'),
    ('meses', 'Meses'),
    ('años', 'Años'),
]

class CalculoFinancieroForm(forms.Form):
    tipo_calculo = forms.ChoiceField(
        choices=TIPO_CALCULO_CHOICES,
        label="Tipo de Cálculo",
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
            'x-data': '{ isOptionSelected: false }',
            '@change': 'isOptionSelected = true',
            ':class': 'isOptionSelected && "text-black dark:text-white"'
        })
    )
    
    tipo_tasa = forms.ChoiceField(
        choices=FRECUENCIA_CHOICES,
        label="Tipo de Tasa",
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
            'x-data': '{ isOptionSelected: false }',
            '@change': 'isOptionSelected = true',
            ':class': 'isOptionSelected && "text-black dark:text-white"'
        })
    )
    
    tipo_capitalizacion = forms.ChoiceField(
        choices=FRECUENCIA_CHOICES,
        label="Tipo de Capitalización",
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
            'x-data': '{ isOptionSelected: false }',
            '@change': 'isOptionSelected = true',
            ':class': 'isOptionSelected && "text-black dark:text-white"'
        })
    )
    
    tipo_periodo = forms.ChoiceField(
        choices=TIPO_PERIODO_CHOICES,
        label="Tipo de Periodo",
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary',
        })
    )
    
    capital = forms.FloatField(
        required=False,
        label="Capital (P)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
    
    pago_periodico = forms.FloatField(
        required=False,
        label="Pago Periódico (R)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
    
    tasa = forms.FloatField(
        label="Tasa de Interés (%)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
    
    periodos = forms.IntegerField(
        label="Número de Periodos (n)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
class FactorCapitalizacionForm(forms.Form):
    tasa = forms.FloatField(
        label="Tasa de Interés (i)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
    
    tipo_tasa = forms.ChoiceField(
        label="Tipo de Tasa",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    tipo_capitalizacion = forms.ChoiceField(
        label="Tipo de Capitalización",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    stock_inicial = forms.FloatField(
        label="Stock Inicial (P)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    periodos = forms.IntegerField(
        label="Número de Periodos (n)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    tipo_periodo = forms.ChoiceField(
        label="Tipo de Periodo",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )


class FactorActualizacionForm(forms.Form):
    tasa = forms.FloatField(
        label="Tasa de Interés (i)",
        widget=forms.NumberInput(attrs={
            'class': 'mb-3 w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )
    
    tipo_tasa = forms.ChoiceField(
        label="Tipo de Tasa",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    tipo_capitalizacion = forms.ChoiceField(
        label="Tipo de Capitalización",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    stock_final = forms.FloatField(
        label="Stock Final (S)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    periodos = forms.IntegerField(
        label="Número de Periodos (n)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )

    tipo_periodo = forms.ChoiceField(
        label="Tipo de Periodo",
        choices=[
            ('Anual', 'Anual'),
            ('Diaria', 'Diaria'),
            ('Semanal', 'Semanal'),
            ('Mensual', 'Mensual'),
            ('Trimestral', 'Trimestral'),
            ('Bimestral', 'Bimestral'),
            ('Semestral', 'Semestral'),
        ],
        widget=forms.Select(attrs={
            'class': 'relative z-20 w-full appearance-none rounded border-[1.5px] border-stroke bg-transparent py-3 pl-5 pr-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary'
        })
    )