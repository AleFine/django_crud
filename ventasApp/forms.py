from django import forms 
from django.forms import fields 
from .models import Categoria
class CategoriaForm(forms.ModelForm):
  class Meta: 
    model=Categoria
    fields=['descripcion','estado']
  
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

class RegistroForm(forms.ModelForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu nombre de usuario'
        })
    )
    email = forms.EmailField(
        label='Nombre de usuario',
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu nombre de usuario'
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
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary',
            'placeholder': 'Ingresa tu contraseña'
        })
    )

