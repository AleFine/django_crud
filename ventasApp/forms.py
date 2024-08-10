from django import forms 
from django.forms import fields 
from .models import Categoria
class CategoriaForm(forms.ModelForm):
  class Meta: 
    model=Categoria
    fields=['descripcion','estado']
  
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Gmail',
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu correo electrónico'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu contraseña'
        })
    )

