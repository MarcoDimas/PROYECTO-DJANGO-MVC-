from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForms


def registros(requets):
    alumnos =Alumnos.objects.all()
    return render(requets, "registros/principal.html", {'9B':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForms()
    return render(request, 'registros/contacto.html', {'form': form})


def contacto(requets):
    return render (requets, "registros/contacto.html")
