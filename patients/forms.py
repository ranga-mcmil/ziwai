from django import forms
from .models import PatientProfile, Prescription
from doctors.models import DoctorProfile

class PatientProfileForm(forms.ModelForm):

    doctor = forms.ModelChoiceField(queryset=DoctorProfile.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    patient_history = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'description',
        }
    ))

    class Meta:
        model = PatientProfile
        fields = ('doctor', 'patient_history')


class PrescriptionForm(forms.ModelForm):

    patient = forms.ModelChoiceField(queryset=PatientProfile.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    notes = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'description',
        }
    ))

    class Meta:
        model = Prescription
        fields = ('patient', 'notes')
