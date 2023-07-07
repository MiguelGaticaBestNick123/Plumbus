from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm, CustomUserCreationForm, frmCrearCuenta, frmContacto
from django.contrib import messages
from .models import Plumbus, Producto, ItemCarrito, Contacto
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
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario = CustomUserCreationForm(data=request.POST)
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, User)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="inicio")
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

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    item, created = ItemCarrito.objects.get_or_create(producto=producto, usuario=request.user)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    items_carrito = ItemCarrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in items_carrito)
    context = {
        'items_carrito': items_carrito,
        'total': total
    }
    return render(request, 'carrito/ver_carrito.html', context)

@login_required
def eliminar_item_carrito(request, item_id):
    item = ItemCarrito.objects.get(pk=item_id)
    item.delete()
    return redirect('ver_carrito')

def contacto(request):
    if request.method == 'POST':
        form = frmContacto(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inicio')
    else:
        form = frmContacto()
    
    contexto = {
        'form': form
    }
    
    return render(request, 'app/contacto.html', contexto)
