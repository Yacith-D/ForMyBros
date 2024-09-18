
# Create your models here.
from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    fecha_ingreso = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

