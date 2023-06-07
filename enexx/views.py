from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'enexx/index.html',context)

def ps5(request):
    context={}
    return render(request, 'enexx/ps5.html',context)