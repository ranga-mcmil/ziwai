from django.contrib import admin
from .models import PatientProfile, Prescription


# Register your models here.
@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'notes', 'date_created')