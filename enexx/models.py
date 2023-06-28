from django.db import models

# Create your models here.
class Consola(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    genero = models.TextField()
    cantidad = models.IntegerField()
    consola = models.ForeignKey(Consola, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, default=50)
    imagen = models.ImageField(upload_to="juegos", null=True)
    def __str__(self) -> str:
        return self.nombre


opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre