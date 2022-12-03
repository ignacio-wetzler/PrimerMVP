from django.db import models

# Create your models here.

class Pariente(models.Model):
    nombre = models.CharField(max_length = 24)
    apellido = models.CharField(max_length = 24)
    edad = models.IntegerField()

    def __str__(self):
        return (f"nombre: {self.nombre} apellido: {self.apellido} edad: {self.edad}")
    