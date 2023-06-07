from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('ps5', views.ps5, name='ps5'),
    path('Switch', views.Switch, name='Switch'),
]