from django.urls import path, include  
from . import views


urlpatterns = [
    path('admin/', views.admin, name='admin'),  
    path('inicio/', views.inicio, name='inicio'),
    
    path('agregar_doctor/', views.Agregar_Doctor, name='agregar_doctor'),
    path('buscar_doctor/', views.Buscar_Doctor, name='buscar_doctor'),
    
    path('agregar_paciente/', views.Agregar_Paciente, name='agregar_paciente'),
    path('buscar_paciente/', views.Buscar_Paciente, name='buscar_paciente'),
    
    path('agregar_habitacion/', views.Agregar_Habitacion, name='agregar_habitacion'),
    path('buscar_habitacion/', views.Buscar_Habitacion, name='buscar_habitacion'),
    
    path('turnos/', views.turnos, name='turnos'),
    
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    """""
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), """
]
