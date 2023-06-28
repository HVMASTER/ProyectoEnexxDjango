from django.contrib import admin
from .models import Consola, Juego, Tipo, Contacto

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'genero', 'cantidad', 'consola', 'tipo')#esto es para que se muestren estos campos en el admin
    list_editable = ('precio', 'cantidad', 'consola', 'tipo') #esto es para que se puedan editar estos campos directamente desde el admin
    search_fields = ('nombre', 'precio')#esto es para que se pueda buscar por nombre y precio
    list_filter = ('genero', 'consola', 'tipo')#esto es para que se pueda filtrar por genero, consola y tipo
    list_per_page = 10 #esto es para que se muestren 10 productos por pagina en el admin

# Register your models here.
admin.site.register(Consola)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Tipo)
admin.site.register(Contacto)#esto es para que se muestren los modelos en el admin
