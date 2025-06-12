from pyexpat.errors import messages
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView



def about(request):
    return render(request, 'aplicacion/about.html')



def index(request):
    return render(request, "aplicacion/inicio.html")

def servicioslist(request):
    return render(request, "aplicacion/NuestrosServicios.html")

#--------------------------------------------------------------------------------------------#
    # Funciones para manejar los doctores siempre y cuando el usuario esté autenticado

def Buscar_Doctor(request):
    query = request.GET.get('nombre', '')
    resultados = Doctor.objects.filter(nombre__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Doctor.html", {"resultados": resultados})

@login_required
def Agregar_Doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            especialidad = form.cleaned_data['especialidad']
            legajo = form.cleaned_data['legajo']
            form.save()
            doctores =  Doctor.objects.all()
            return render(request, "aplicacion/Agregar_doctor.html", {"doctores": doctores})
    else:
        form = DoctorForm()
    return render(request, "aplicacion/doctor_form.html", {"form": form})

#--------------------------------------------------------------------------------------------#
#Funciones para manejar los pacientes siempre y cuando el usuario esté autenticado

@login_required
def Agregar_Paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            historia = form.cleaned_data['historia']
            form.save()
            pacientes = Paciente.objects.all()
            return render(request, "aplicacion/Agregar_Paciente.html", {"pacientes": pacientes})
    else:
        form = PacienteForm()
    return render(request, "aplicacion/Agregar_Paciente.html", {"form": form})

@login_required
def Buscar_Paciente(request):
    query = request.GET.get('nombre', '')
    resultados = Paciente.objects.filter(nombre__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Paciente.html", {"resultados": resultados})
#--------------------------------------------------------------------------------------------#
# Funciones para manejar las habitaciones siempre y cuando el usuario esté autenticado

@login_required
def Agregar_Habitacion(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            tipo = form.cleaned_data['tipo']
            disponible = form.cleaned_data['disponible']
            form.save()
            habitaciones = Habitacion.objects.all()
            return render(request, "aplicacion/Agregar_Habitacion.html", {"habitaciones": habitaciones})
    else:
        form = HabitacionForm()
    return render(request, "aplicacion/Agregar_Habitacion.html", {"form": form})

@login_required
def Buscar_Habitacion(request):
    query = request.GET.get('numero', '')
    resultados = Habitacion.objects.filter(numero__icontains=query) if query else None
    return render(request, "aplicacion/Buscar_Habitacion.html", {"resultados": resultados})


@login_required
def turno(request):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            
            paciente     = form.cleaned_data['paciente']
            doctor       = form.cleaned_data['doctor']
            fecha_turno  = form.cleaned_data['fecha_turno']
            motivo       = form.cleaned_data['motivo_consulta']
            estado       = form.cleaned_data['estado']

            
            Turno.objects.create(
                paciente=paciente,
                doctor=doctor,
                fecha_turno=fecha_turno,
                motivo_consulta=motivo,
                estado=estado
            )
            messages.success(request, "Turno agregado correctamente.")
            return redirect('aplicacion:turno_list')
    else:
        form = TurnoForm()

    return render(request, "aplicacion/turno.html", {
        "form": form,
    })

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
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


# __________________________________ CBV CRUD ___________________________________________________

#Funciones basadas en clases para manejar los doctores, pacientes, habitaciones y turnos, siempre y cuando el usuario esté autenticado

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "fecha_ingreso", "fecha_salida", "historia_clinica"]
    success_url = reverse_lazy("pacientes")

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    fields = ["nombre", "apellido", "edad", "fecha_ingreso", "fecha_salida", "historia_clinica"]
    success_url = reverse_lazy("pacientes")

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy("pacientes")
    
    
    
class DoctorList(LoginRequiredMixin, ListView):
    model = Doctor

class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    fields = ["nombre", "apellido", "especialidad", "legajo"]
    success_url = reverse_lazy("doctorlist")

class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = Doctor
    fields = ["nombre", "apellido", "especialidad", "legajo"]
    success_url = reverse_lazy("doctorlist")

class DoctorDelete(LoginRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctorlist")

class HabitacionList(LoginRequiredMixin, ListView):
    model = Habitacion

class HabitacionCreate(LoginRequiredMixin, CreateView):
    model = Habitacion
    fields = ["numero", "tipo", "disponible"]
    success_url = reverse_lazy("habitacion")

class HabitacionUpdate(LoginRequiredMixin, UpdateView):
    model = Habitacion
    fields = ["numero", "tipo", "disponible"]
    success_url = reverse_lazy("habitacion")

class HabitacionDelete(LoginRequiredMixin, DeleteView):
    model = Habitacion
    success_url = reverse_lazy("habitacion")



class TurnoList(LoginRequiredMixin, ListView):
    model = Turno

class TurnoCreate(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ["paciente", "doctor", "fecha_turno", "motivo_consulta", "estado"]
    success_url = reverse_lazy("aplicacion:turno_list")

class TurnoUpdate(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ["paciente", "doctor", "fecha_turno", "motivo_consulta", "estado"]
    success_url = reverse_lazy("turno")

class TurnoDelete(LoginRequiredMixin, DeleteView):
    model = Turno
    success_url = reverse_lazy("turno")

# _______________ Registracion / Login / Logout __________________

# login personalizado
class UserLoginView(LoginView):

    template_name = 'aplicacion/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('aplicacion:inicio')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada correctamente. Ahora puedes iniciar sesión.")
            return redirect('aplicacion:login')
    else:
        form = UserCreationForm()

    return render(request, 'aplicacion/registro.html', {'form': form})



def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________            
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

# ___________  edit Perfil de usuario ______________

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("index"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editar_perfil.html", {"form": miForm})

@login_required
def AgregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("index"))
    else:
        miForm = AvatarForm()
    return render(request, "aplicacion/AgregarAvatar.html", {"form": miForm})    