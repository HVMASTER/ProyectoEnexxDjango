from django.shortcuts import render
from .models import Juego, Tipo
# Create your views here.




def index(request):
    context={}
    return render(request, 'enexx/home.html',context)

def ps5(request):
    context={}
    juego = Juego.objects.filter(tipo__nombre='fisico',consola__nombre='PS5')
    data = {        
        'juego': juego
    }
    return render(request, 'enexx/ps5.html',data)
    return render(request, 'enexx/ps5.html',context)

def Switch(request):
    context={}
    return render(request, 'enexx/Switch.html',context)

def xbox_fisicos(request):
    context={}
    return render(request, 'enexx/xbox_fisicos.html',context)

def ps5digital(request):
    context={}
    juego = Juego.objects.filter(tipo__nombre='digital',consola__nombre='PS5')
    data = {        
        'juego': juego
    }
    return render(request, 'enexx/ps5digital.html',data)
    return render(request, 'enexx/ps5digital.html',context)

def Switch_digital(request):
    context={}
    return render(request, 'enexx/Switch_digital.html',context)

def xbox_digital(request):
    context={}
    return render(request, 'enexx/xbox_digital.html',context)

def ps5dlc(request):
    context={}
    juego = Juego.objects.filter(tipo__nombre='dlc',consola__nombre='PS5')
    data = {        
        'juego': juego
    }
    return render(request, 'enexx/ps5digital.html',data)
    return render(request, 'enexx/ps5dlc.html',context)

def Switch_dlc(request):
    context={}
    return render(request, 'enexx/Switch_dlc.html',context)

def xbox_dlc(request):
    context={}
    return render(request, 'enexx/xbox_dlc.html',context)

def inicioSesion(request):
    context={}
    return render(request, 'enexx/inicioSesion.html',context)

def crearUsuario(request):
    context={}
    return render(request, 'enexx/crearUsuario.html',context)