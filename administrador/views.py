from django.shortcuts import render, redirect
from enexx.models import Juego, Tipo
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def menu(request):
    context={}
    return render(request, 'administrador/menu.html',context)

def registro(request):
    
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="menu")
        data['form'] = formulario

    return render(request, 'administrador/registro.html',data)

