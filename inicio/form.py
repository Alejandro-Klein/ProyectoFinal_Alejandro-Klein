from django import forms 
from usuario.form import MiFormularioDeEdicionDeDatosDeUsuario

# NOTA: Se relacio0na con el modelo que quiero crear. es decir con models.py.
# , widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y') asi seria el formato de argentina pa la fecha pero no me lo caarga al modificar usando esta forma!

# class CrearAlumnoFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20)
#     materia = forms.CharField(max_length=20)
#     nota = forms.IntegerField(required=False)
#     fecha_examen = forms.DateField(required=False)
    
    
    
class BusquedaAlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
