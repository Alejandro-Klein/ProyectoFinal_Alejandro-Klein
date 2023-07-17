from django.shortcuts import render
from inicio.form import BusquedaAlumnoFormulario
from inicio.models import Alumno
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from usuario.form import MiFormularioDeEdicionDeDatosDeUsuario
# from usuario.models import User
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

# @login_required
# def crear_alumno(request):
#     mensaje = ''
    
#     if request.method == 'POST':
#         formulario = CrearAlumnoFormulario(request.POST)
#         if formulario.is_valid():
#            info = formulario.cleaned_data
#            alumno = Alumno(nombre=info['nombre'],materia=info['materia'],nota=info['nota'],fecha_examen=info['fecha_examen'],descripcion=info['descripcion'])
#            alumno.save()
#            mensaje = f'Se cargo alumno/a {alumno.nombre}'
#         else:    
#            return render(request, 'inicio/crear_alumno.html',{'formulario':formulario})
        
        
#     formulario = CrearAlumnoFormulario()
#     return render(request, 'inicio/crear_alumno.html',{'formulario':formulario , 'mensaje' : mensaje})

def about(request):
    return render(request, 'inicio/about.html')

def listar_alumnos(request):
    
    formulario = BusquedaAlumnoFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre','')
        lista_alumnos = Alumno.objects.filter(nombre__icontains=nombre_a_buscar)
    
    
    
    formulario = BusquedaAlumnoFormulario()
    return render(request,'inicio/alumnos.html',{'formulario':formulario,'lista_alumnos':lista_alumnos})

#CLASES BASADAS EN VISTA (CBV)

class DetalleAlumno(DetailView):
    model = Alumno
    template_name = "inicio/detalle_alumno.html"
    

class ModificarAlumno(LoginRequiredMixin,UpdateView):
    model = Alumno
    fields = ['nombre','materia','nota','fecha_examen','descripcion','imagen_alumno']
    template_name = "inicio/modificar_alumno.html"
    success_url = reverse_lazy('inicio:alumnos')
    
class EliminarAlumno(LoginRequiredMixin,DeleteView):
    model = Alumno
    template_name = "inicio/eliminar_alumno.html"
    success_url = reverse_lazy('inicio:alumnos')

class CrearAlumno(LoginRequiredMixin,CreateView):
    model = Alumno
    template_name = "inicio/crear_alumno.html"
    fields = ['nombre','materia','nota','fecha_examen','descripcion','imagen_alumno']
    success_url = reverse_lazy('inicio:alumnos')

class DetalleUsuario(LoginRequiredMixin,DetailView):
    model = User
    template_name = "inicio/datos_usuario.html"