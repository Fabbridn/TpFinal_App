from django.shortcuts import render

from .models import *
from . forms import *


def Agregar_Doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especialidad = form.cleaned_data['especialidad']
            legajo = form.cleaned_data['legajo']
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
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            historia = form.cleaned_data['historia']
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
            numero = form.cleaned_data['numero']
            tipo = form.cleaned_data['tipo']
            disponible = form.cleaned_data['disponible']
            form.save()
    else:
        form = HabitacionForm()
    return render(request, "aplicacion/Agregar_Habitacion.html", {"form": form})

def Buscar_Habitacion(request):
    query = request.GET.get('numero', '')
    resultados = Habitacion.objects.filter(numero__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Habitacion.html", {"resultados": resultados})


def turnos(request):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data['paciente']
            doctor = form.cleaned_data['doctor']
            fecha = form.cleaned_data['fecha']
            form.save()
    else:
        form = TurnoForm()
    return render(request, "aplicacion/turnos.html", {"form": form})

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # Aquí podrías guardar el mensaje en la base de datos o enviar un correo
        print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")
    return render(request, "aplicacion/contacto.html")

def nosotros(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # Aquí podrías guardar el mensaje en la base de datos o enviar un correo
        print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")
    return render(request, "aplicacion/nosotros.html")
