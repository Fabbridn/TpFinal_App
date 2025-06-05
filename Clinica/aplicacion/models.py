from django.db import models


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad}"

class Habitacion(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True or False)

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - {'Disponible' if self.disponible else 'Ocupada'}"

class Turnos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_turno = models.DateTimeField()
    motivo_consulta = models.TextField()

    def __str__(self):
        return f"Turno: {self.fecha_turno} - Paciente: {self.paciente} - Doctor: {self.doctor}"