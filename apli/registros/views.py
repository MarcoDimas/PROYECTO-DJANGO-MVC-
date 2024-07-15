from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForms
from .forms import ComentarioContacto
from django.shortcuts import get_object_or_404

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
