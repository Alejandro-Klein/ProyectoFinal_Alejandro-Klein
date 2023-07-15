from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    materia = models.CharField(max_length=20)
    nota = models.IntegerField(null=True)
    fecha_examen = models.DateField(null=True)
    #descripcion = models.TextField(null=True,max_length=1000, help_text="Ingrese una breve descripción del alumno")
 
    def __str__(self):
       return f'Nombre: {self.nombre} - Materia: {self.materia} - Nota: {self.nota} '
      
 


