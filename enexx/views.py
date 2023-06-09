from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego, Tipo
from .forms import ContactoFrom, JuegoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.




def index(request):
    context={}
    return render(request, 'enexx/home.html',context)

def ps5(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='fisico',consola__nombre='PS5')
    data = {        
        'juegos': juegos
    }
    return render(request, 'enexx/ps5.html',data)
    return render(request, 'enexx/ps5.html',context)

def Switch(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='fisico',consola__nombre='SWITCH')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/Switch.html',data)
    return render(request, 'enexx/Switch.html',context)

def xbox_fisicos(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='fisico',consola__nombre='XBOX')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/xbox_fisicos.html',data)
    return render(request, 'enexx/xbox_fisicos.html',context)

def ps5digital(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='digital',consola__nombre='PS5')
    data = {        
        'juegos': juegos
    }
    return render(request, 'enexx/ps5digital.html',data)
    return render(request, 'enexx/ps5digital.html',context)

def Switch_digital(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='digital',consola__nombre='SWITCH')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/Switch_digital.html',data)
    return render(request, 'enexx/Switch_digital.html',context)

def xbox_digital(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='digital',consola__nombre='XBOX')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/xbox_digital.html',data)
    return render(request, 'enexx/xbox_digital.html',context)

def ps5dlc(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='dlc',consola__nombre='PS5')
    data = {        
        'juegos': juegos
    }
    return render(request, 'enexx/ps5digital.html',data)
    return render(request, 'enexx/ps5dlc.html',context)

def Switch_dlc(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='dlc',consola__nombre='SWITCH')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/Switch_dlc.html',data)
    return render(request, 'enexx/Switch_dlc.html',context)

def xbox_dlc(request):
    context={}
    juegos = Juego.objects.filter(tipo__nombre='dlc',consola__nombre='XBOX')
    data = {
        'juegos': juegos
    }
    return render(request, 'enexx/xbox_dlc.html',data)
    return render(request, 'enexx/xbox_dlc.html',context)

def inicioSesion(request):
    context={}
    return render(request, 'enexx/inicioSesion.html',context)

def crearUsuario(request):
    context={}
    return render(request, 'enexx/crearUsuario.html',context)


def contacto(request):
    data = {
        'form': ContactoFrom()
    }

    if request.method == 'POST':#si el metodo es post se guardan los datos del formulario
        formulario = ContactoFrom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado correctamente")
        else:
            data['form'] = formulario
    return render(request, 'enexx/contacto.html', data)
