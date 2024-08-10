from django import forms 
from django.forms import fields 
from .models import Categoria
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