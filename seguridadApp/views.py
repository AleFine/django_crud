from typing import Generic
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from ventasApp.forms import LoginForm
def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("homePage")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def ingresar_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username= user, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('homePage')  
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos") 
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})

def register(request):
    return render(request, 'register.html')

def homePage(request):
    context = {}
    return render(request, "index.html", context)
def salir(request): 
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login") 