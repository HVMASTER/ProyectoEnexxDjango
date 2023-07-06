from django.shortcuts import render, redirect, get_object_or_404
from enexx.models import Juego, Tipo
from .forms import CustomUserCreationForm
from enexx.forms import JuegoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required #decorador para que solo el staff pueda acceder a esta vista
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
@permission_required('staff') #decorador para que solo el staff pueda acceder a esta vista
def menu(request):

    return render(request, 'administrador/menu.html')

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

@permission_required('enexx.add_juego')
def agregarJuego(request):
    data = {
        'form': JuegoForm()
    }
    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Juego guardado correctamente")
        else:
            data['form'] = formulario
    return render(request, 'administrador/agregarJuego.html', data)

@permission_required('enexx.view_juego')
def listarJuego(request):

    juego = Juego.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(juego, 10)
        juego = paginator.page(page)
    except:
        raise Http404

    data={
        'juegos': juego,
        'paginator': paginator
    }

    return render(request, 'administrador/listarJuego.html', data)
    
@permission_required('enexx.change_juego')
def modificarJuego(request, id):
    
    juego = get_object_or_404(Juego, id=id)

    data = {
        'form': JuegoForm(instance=juego) #instance es para que se muestren los datos en el formulario
    }
    if request.method == 'POST':
        formulario = JuegoForm(data=request.POST, instance=juego, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Juego Editado Correctamente")
            return redirect(to="listarJuego")
        else:
            data['form'] = formulario


    return render(request, 'administrador/modificarJuego.html', data)

@permission_required('enexx.delete_juego')
def eliminarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    messages.success(request, "Juego Eliminado Correctamente")
    return redirect(to="listarJuego")

