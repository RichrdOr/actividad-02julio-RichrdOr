from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula, Estudiante, Modulo
from administrativo.forms import MatriculaForm, MatriculaEditForm
from administrativo.forms import ModuloForm, EstudianteForm

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    """
    """
    matriculas = Matricula.objects.all()

    titulo = "Listado de matriculas"
    informacion_template = {'matriculas': matriculas,'numero_matriculas': len(matriculas), 'mititulo': titulo}
    return render(request, 'index.html', informacion_template)


def detalle_matricula(request, id):
    """

    """

    matricula = Matricula.objects.get(pk=id)
    informacion_template = {'matricula': matricula}
    return render(request, 'detalle_matricula.html', informacion_template)


def crear_matricula(request):
    """
    """
    if request.method=='POST':
        formulario = MatriculaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MatriculaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)

def editar_matricula(request, id):
    """
    """
    matricula = Matricula.objects.get(pk=id)
    print("----------matricula")
    print(matricula)
    print("----------matricula")
    if request.method=='POST':
        formulario = MatriculaEditForm(request.POST, instance=matricula)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MatriculaEditForm(instance=matricula)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_matricula.html', diccionario)

def detalle_estudiante(request, id):
    """

    """

    estudiante = Estudiante.objects.get(pk=id)
    informacion_template = {'e': estudiante}
    return render(request, 'detalle_estudiante.html', informacion_template)

# ver los módulos
#    nombre del módulp
#    valor de todas las matriculas del módulo    
# ver los estudiantes >> de los estudiantes debo visualizar:
#    nombre 
#    apellido
#    cedula
#    edad
#    tipo_estudiante 
#    costo de matriculas

# crear módulos
# crear estudiantes

def crear_modulo(request):
    print("crear_modulo")
    if request.method == 'POST':
        form = ModuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = ModuloForm()
    return render(request, 'crear_modulo.html', {'formulario': form})


def crear_estudiante(request):
    print("crear_estudiante")
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'formulario': form})


def listar_Estudiante(request):
    estudiantes = Estudiante.objects.all()
    numero_estudiantes = len(estudiantes)
    return render(request, 'listar_estudiantes.html', {'estudiantes': estudiantes, 'numero_estudiantes': numero_estudiantes})    


def listar_modulo(request):
    modulos = Modulo.objects.all()
    numero_modulos = len(modulos)
    return render(request, 'listar_modulos.html', {'modulos': modulos, 'numero_modulos': numero_modulos})    