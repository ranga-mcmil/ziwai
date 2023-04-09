from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django_resized import ResizedImageField

BLOOD_GROUPS = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
)

SEX = (
    ("Male", "Male"),
    ("Female", "Female"),    
)

USER_TYPE = (
    ("Patient", "Patient"),
    ("Doctor", "Doctor"),  
    ("Receptionist", "Receptionist"),   
)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.CharField(max_length=250, null=True, unique=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=True, blank=True, choices=BLOOD_GROUPS)
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default='Receptionist')
    date_of_birth = models.DateField(null=True, blank=True)
    pic = ResizedImageField(size=[600, 600], crop=['top', 'left'], upload_to='images/')
    sex = models.CharField(max_length=10, choices=SEX, null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

