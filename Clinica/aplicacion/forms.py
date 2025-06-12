from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Paciente, Habitacion
from django.contrib.auth.forms import UserChangeForm

class DoctorForm(forms.Form):
    nombre = forms.CharField(max_length=12, label= "Nombre del Médico", required=True)
    apellido = forms.CharField(max_length=15, label= "Apellido del Médico", required=True)
    especialidad = forms.CharField(max_length=100, label= "Especialidad del Médico", required=True)
    legajo = forms.CharField(max_length=20, label= "Legajo del Médico", required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  

class PasswordChangeForm(UserChangeForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["password", "password2"]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)      

class PacienteForm(forms.Form):
    nombre =  forms.CharField(max_length=12, label= "Nombre del Paciente", required=True)
    apellido = forms.CharField(max_length=15, label= "Apellido del Paciente", required=True)
    edad = forms.IntegerField(label= "Edad del Paciente", required=True)
    historia = forms.CharField(max_length=100, label= "Historia Clinica del Paciente", required=True)

class HabitacionForm(forms.Form):
    numero = forms.IntegerField(label= "Número de la Habitación", required=True)
    tipo = forms.CharField(max_length=50, label= "Tipo de Habitación", required=True)
    disponible = forms.BooleanField(label= "¿Está disponible?", required=False, initial=True)

    
class TurnoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(),label="Paciente",required=True,widget=forms.Select)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(),label="Médico",required=True,widget=forms.Select)
    fecha_turno = forms.DateField(label="Fecha del Turno",required=True,widget=forms.DateInput(attrs={'type': 'date'}))
    motivo_consulta = forms.CharField(widget=forms.Textarea,label="Motivo de la Consulta",required=True)
    estado = forms.ChoiceField(choices=[("pendiente", "Pendiente"),("confirmado", "Confirmado"),("cancelado", "Cancelado")],label="Estado del Turno",required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido}"

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje", required=True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("El email debe ser de la forma '@example.com'")
        return email