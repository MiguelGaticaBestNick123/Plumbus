from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm
# Create your views here.
@login_required
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