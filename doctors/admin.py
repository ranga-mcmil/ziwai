from django.contrib import admin
from .models import DoctorProfile

# Register your models here.
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')