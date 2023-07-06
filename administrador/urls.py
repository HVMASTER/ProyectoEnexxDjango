from django.urls import path
from . import views



urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('registro', views.registro, name='registro'),
    path('agregarJuego', views.agregarJuego, name='agregarJuego'),
    path('listarJuego', views.listarJuego, name='listarJuego'),
    path('modificarJuego/<id>', views.modificarJuego, name='modificarJuego'),
    path('eliminarJuego/<id>', views.eliminarJuego, name='eliminarJuego'),
    

]