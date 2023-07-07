from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm
from .models import Plumbus
# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def loginsexo(request):
    
    contexto = {
        "form": LoginForm()
    }
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            name_user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=name_user, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
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