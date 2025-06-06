from django.contrib import admin

# Register your models here.
from .models import Doctor, agregar_paciente, Habitacion, Turno, Contacto, Nosotros, Inicio, Index, Login, Logout

admin.site.register(Doctor)
admin.site.register(agregar_paciente)
admin.site.register(Habitacion)
admin.site.register(Turno)
admin.site.register(Contacto)
admin.site.register(Nosotros)
admin.site.register(Inicio)
admin.site.register(Index)
admin.site.register(Login)
admin.site.register(Logout)
