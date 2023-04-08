from django.db import models
from accounts.models import User

# Create your models here.
DEPARTMENTS = (
    ("Dept 1", "Dept 1"),
    ("Dept 2", "Dept 2"),    
)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor_profile")
    department = models.CharField(max_length=20, choices=DEPARTMENTS)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'