
from django.db import models
from .models import *

from django import forms

import datetime


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

class agregar_doctorForm(forms.Form):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    legajo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Agregar Doctor: {self.nombre} {self.apellido} - {self.especialidad}"

class agregar_paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)
    historia_clinica = models.TextField()
    
    def __str__(self):
        return f"Agregar Paciente: {self.nombre} {self.apellido} - Edad: {self.edad}"

class Habitacion(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True or False)

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - {'Disponible' if self.disponible else 'Ocupada'}"

class Turno(models.Model):
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    ESTADOS_TURNO = [
        ("pendiente", "Pendiente"),
        ("confirmado", "Confirmado"),
        ("cancelado", "Cancelado"),
    ]

    paciente = models.ForeignKey(agregar_paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_turno = models.DateTimeField()
    motivo_consulta = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADOS_TURNO, default="pendiente")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Turno con {self.doctor} para {self.paciente} el {self.fecha_turno.strftime('%d-%m-%Y %H:%M')}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f"Contacto: {self.apellido} - Email: {self.email}"
    
class Nosotros(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return f"Nosotros: {self.descripcion[:50]}..."  # Mostrar solo los primeros 50 caracteres

