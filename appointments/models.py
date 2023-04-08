from django.db import models
from accounts.models import User
from doctors.models import DoctorProfile
from patients.models import PatientProfile


STATUS = (
    ("Pending", "Pending"),
    ("Cancelled", "Cancelled"),
    ("Done", "Done"),      
)

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="appointments")
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS)

    
    def __str__(self):
        return f'{self.patient.user.first_name} {self.patient.user.last_name} Appointment'