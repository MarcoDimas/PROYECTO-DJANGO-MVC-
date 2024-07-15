from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForms
from .forms import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime

def registros(requets):
    alumnos =Alumnos.objects.all()
    return render(requets, "registros/principal.html", {'9B':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForms(request.POST)
        if form.is_valid():
            form.save()

            comentarios=ComentarioContacto.objects.all()
            return render(request, 'registros/comentario.html',
                        {'9B':comentarios})
    form = ComentarioContactoForms()
    return render(request, 'registros/contacto.html', {'form': form})


def contacto(requets):
    return render (requets, "registros/contacto.html")


def comentario(requets):
    comentarios =ComentarioContacto.objects.all()
    return render(requets, "registros/comentario.html", {'9B':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/contacto.html",  {'9B':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(requets, id): 
    comentarios =ComentarioContacto.objects.get(id=id)
    return render(requets, "registros/editarComentario.html", {'9B':comentarios})


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForms(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/comentario.html", {'9B': comentarios})
    else:
        form = ComentarioContactoForms(instance=comentario)
    
    return render(request, "registros/editarComentario.html", {'form': form, 'comentario': comentario})


def consulta1(requets):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(requets, "registros/consultas.html", {'9B':alumnos})


def consulta2(requets):
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(requets, "registros/consultas.html", {'9B':alumnos})

def consulta3(requets):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(requets, "registros/consultas.html", {'9B':alumnos})

def consulta4(requets):
    alumnos = Alumnos.objects.filter(turno__contains="Vesp")
    return render(requets, "registros/consultas.html", {'9B':alumnos})

def consulta5(requets):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(requets, "registros/consultas.html", {'9B':alumnos})


def consulta6(requets):
    fechaInicio = datetime.date(2024, 7, 1)
    fechaFin = datetime.date(2024, 7, 13)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(requets, "registros/consultas.html", {'9B':alumnos})

def consulta7(requets):
    alumnos = Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render(requets, "registros/consultas.html", {'9B':alumnos})

