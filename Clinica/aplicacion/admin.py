from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Doctor)
admin.site.register(agregar_paciente)
admin.site.register(Habitacion)
admin.site.register(Turno)
admin.site.register(Contacto)

