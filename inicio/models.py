from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    nota = models.IntegerField(null=True)
