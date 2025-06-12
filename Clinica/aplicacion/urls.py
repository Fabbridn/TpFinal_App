from django.urls import * 

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView, PasswordChangeView 
from django.contrib.auth import views as auth_views
from . import views
from .models import *
from django.urls import reverse_lazy

app_name = 'aplicacion'
    
urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('about/', views.about, name='about'),

   # path('page/<int:pk>/', views.page, name='page'),

    path('doctor/', views.Doctor, name='doctor'),
    path('agregar_doctor/', views.Agregar_Doctor, name='agregar_doctor'),
    path('buscar_doctor/', views.Buscar_Doctor, name='buscar_doctor'),
    path('doctor_form/', views.DoctorForm, name='doctor_form'),
    path("doctorlist/", views.DoctorList.as_view() , name="doctorlist"),
    path("doctorCreate/",  views.DoctorCreate.as_view() , name="doctorCreate"),
    path("doctorUpdate/<int:pk>/", views.DoctorUpdate.as_view() , name="doctorUpdate"),
    path("doctorDelete/<int:pk>/", views.DoctorDelete.as_view() , name="doctorDelete"),      
    

    path('agregar_paciente/', views.Agregar_Paciente, name='agregar_paciente'),
    path('buscar_paciente/', views.Buscar_Paciente, name='buscar_paciente'),
    path('paciente_form/', views.PacienteForm, name='paciente_form'),
    path("paciente/", views.PacienteList.as_view() , name="paciente"),
    path("pacienteCreate/", views.PacienteCreate.as_view() , name="pacienteCreate"),
    path("pacienteUpdate/<int:pk>/", views.PacienteUpdate.as_view() , name="pacienteUpdate"),
    path("pacienteDelete/<int:pk>/", views.PacienteDelete.as_view() , name="pacienteDelete"),
    
    
    path('agregar_habitacion/', views.Agregar_Habitacion, name='agregar_habitacion'),
    path('habitacion_form/', views.HabitacionForm, name='habitacion_form'),
    path("habitaciones/", views.HabitacionList.as_view(), name="habitaciones"),
    path("habitacionCreate/", views.HabitacionCreate.as_view(), name="habitacionCreate"),
    path("habitacionUpdate/<int:pk>/", views.HabitacionUpdate.as_view(), name="habitacionUpdate"),
    path("habitacionDelete/<int:pk>/", views.HabitacionDelete.as_view(), name="habitacionDelete"), 

    path('servicioslist/', views.servicioslist, name='servicioslist'),
    
    path('turno/', views.turno, name='turno'),
    path('turno_form/', views.TurnoForm, name='turno_form'),
    path("turno_list/", views.TurnoList.as_view(), name="turno_list"),
    path("turnoCreate/", views.TurnoCreate.as_view(template_name='aplicacion/turno_form.html'), name="turnoCreate"),
    path("turnoUpdate/<int:pk>/", views.TurnoUpdate.as_view(), name="turnoUpdate"),
    path("turnoDelete/<int:pk>/", views.TurnoDelete.as_view(), name="turnoDelete"),


    path('contacto_form/', views.ContactoForm, name='contacto_form'),
    path('contacto/', views.contacto, name='contacto'),

    path('nosotros/', views.nosotros, name='nosotros'),

    path('registro/', views.register, name='registro'),
    path('login/', LoginView.as_view(template_name='aplicacion/login.html',next_page=reverse_lazy('aplicacion:index')), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('aplicacion:index')), name='logout'),
    path('password/change/', auth_views.PasswordChangeView.as_view(template_name='aplicacion/password_change.html'), name='password_change'),
    path('perfil/', views.editarPerfil, name='perfil'),
    path('agregarAvatar/', views.AgregarAvatar, name='agregarAvatar'),

] 

#path('admin/', views.admin, name='admin'),