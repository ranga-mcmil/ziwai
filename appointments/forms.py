from django import forms
from .models import Appointment, STATUS
from doctors.models import DoctorProfile
from patients.models import PatientProfile

class AppointmentForm(forms.ModelForm):

    patient = forms.ModelChoiceField(queryset=PatientProfile.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    doctor = forms.ModelChoiceField(queryset=DoctorProfile.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))


    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'status', 'date_time')
        widgets = {
            'date_time': forms.TextInput(
                attrs={'type': 'datetime-local'}
            )
        }
