from django import forms

class DoctorForm(forms.Form):
    nombre = forms.CharField(max_length=12, label= "Nombre del Médico", required=True)
    apellido = forms.CharField(max_length=15, label= "Apellido del Médico", required=True)
    especialidad = forms.CharField(max_length=100, label= "Especialidad del Médico", required=True)

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
    paciente = forms.ModelChoiceField(queryset=None, label="Paciente", required=True)
    doctor = forms.ModelChoiceField(queryset=None, label="Médico", required=True)
    fecha_turno = forms.DateTimeField(label="Fecha y Hora del Turno", required=True)
    motivo_consulta = forms.CharField(widget=forms.Textarea, label="Motivo de la Consulta", required=True)
    estado = forms.ChoiceField(choices=[("pendiente", "Pendiente"), ("confirmado", "Confirmado"), ("cancelado", "Cancelado")], label="Estado del Turno", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].queryset = PacienteForm.objects.all()
        self.fields['doctor'].queryset = DoctorForm.objects.all()

