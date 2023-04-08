from django.contrib import admin
from .models import InvoiceItem, Invoice, Payment


# Register your models here.
@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_created', 'due_date', 'status')

@admin.register(Payment)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('amount', 'invoice', 'patient', 'date_created')