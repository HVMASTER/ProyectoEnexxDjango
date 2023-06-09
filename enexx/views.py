from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'enexx/index.html',context)

def ps5(request):
    context={}
    return render(request, 'enexx/ps5.html',context)

def Switch(request):
    context={}
    return render(request, 'enexx/Switch.html',context)

def xbox_fisicos(request):
    context={}
    return render(request, 'enexx/xbox_fisicos.html',context)

def ps5digital(request):
    context={}
    return render(request, 'enexx/ps5digital.html',context)

def Switch_digital(request):
    context={}
    return render(request, 'enexx/Switch_digital.html',context)