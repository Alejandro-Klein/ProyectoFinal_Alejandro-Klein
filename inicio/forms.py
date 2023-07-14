from django import forms 

# NOTA: Se relacio0na con el modelo que quiero crear. es decir con models.py.

class CrearAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    materia = forms.CharField(max_length=20)
    nota = forms.IntegerField(required=False)
    
    