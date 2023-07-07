from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm, CustomUserCreationForm, frmCrearCuenta
from django.contrib import messages
from .models import Plumbus
# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def loginsexo(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = LoginForm(request)
    
    contexto = {
        "form": form
    }
    
    return render(request, 'app/registration/login.html', contexto)
def tienda(request):
    plumbus = Plumbus.objects.all()
    contexto = {
        "data":plumbus
    }
    return render (request, 'app/tienda.html', contexto)

def registro(request):  
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        if formulario.is_valid():
            formulario = CustomUserCreationForm(data=request.POST)
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, User)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'app/registration/registro.html', data)

def logout_view(request):
    logout(request)
    return redirect('inicio')

def crearcuenta(request):
    form=frmCrearCuenta()
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=frmCrearCuenta(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")

    return render(request,"registration/crearcuenta.html",contexto)