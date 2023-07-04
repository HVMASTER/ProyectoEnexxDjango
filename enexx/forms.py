from django import forms
from .models import Contacto, Juego
from django.contrib.auth.forms import UserCreationForm


class ContactoFrom(forms.ModelForm):

    
    


    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'tipo_consulta', 'mensaje', 'avisos']#esto es para que se muestren estos campos en el formulario
        

class JuegoForm(forms.ModelForm):
    
        nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        genero = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        imagen = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
        
    
        class Meta:
            model = Juego
            fields = ['nombre', 'precio', 'genero', 'cantidad', 'consola', 'tipo', 'imagen']#esto es para que se muestren estos campos en el formulario

