from django.shortcuts import render

from django.shortcuts import render
from . import render
from django.shortcuts import render
from .models import Doctor, Paciente, Habitacion
from . forms import DoctorForm, PacienteForm, HabitacionForm


def inicio(request):
    return render(request, "aplicacion/inicio.html")


def Agregar_Doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DoctorForm()
    return render(request, "aplicacion/Agregar_doctor.html", {"form": form})

def Buscar_Doctor(request):
    query = request.GET.get('nombre', '')
    resultados = Doctor.objects.filter(nombre__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Doctor.html", {"resultados": resultados})

#--------------------------------------------------------------------------------------------#

def Agregar_Paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PacienteForm()
    return render(request, "aplicacion/Agregar_Paciente.html", {"form": form})

def Buscar_Paciente(request):
    query = request.GET.get('nombre', '')
    resultados = Paciente.objects.filter(nombre__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Paciente.html", {"resultados": resultados})
#--------------------------------------------------------------------------------------------#

def Agregar_Habitacion(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HabitacionForm()
    return render(request, "aplicacion/Agregar_Habitacion.html", {"form": form})

def Buscar_Habitacion(request):
    query = request.GET.get('numero', '')
    resultados = Habitacion.objects.filter(numero__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Habitacion.html", {"resultados": resultados})


def turnos(request):
    return render(request, "aplicacion/turnos.html")

def contacto(request):
    return render(request, "aplicacion/contacto.html")

def nosotros(request):
    return render(request, "aplicacion/nosotros.html")

def login(request):
    return render(request, "aplicacion/login.html")