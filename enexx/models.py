from django.db import models

# Create your models here.
class Consola(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    genero = models.TextField()
    consola = models.ForeignKey(Consola, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nombre
