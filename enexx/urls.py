from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('ps5', views.ps5, name='ps5'),
    path('Switch', views.Switch, name='Switch'),
    path('xbox_fisicos', views.xbox_fisicos, name='xbox_fisicos'),
    path('ps5digital', views.ps5digital, name='ps5digital'),
]