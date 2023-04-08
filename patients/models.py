from django.db import models
from accounts.models import User
from doctors.models import DoctorProfile

# Create your models here.
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="patients")
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    patient_history = models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Prescription(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="prescriptions")
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="prescriptions")
    notes = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.patient.user.first_name} {self.patient.user.last_name} Prescription'