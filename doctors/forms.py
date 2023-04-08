from django import forms
from .models import DoctorProfile, DEPARTMENTS

class DoctorProfileForm(forms.ModelForm):

    department = forms.ChoiceField(choices=DEPARTMENTS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = DoctorProfile
        fields = ('department', )
