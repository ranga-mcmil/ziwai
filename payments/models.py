from django.db import models
from patients.models import PatientProfile

STATUS = (
    ("Paid", "Paid"),
    ("Not Paid", "Not Paid"),
)

class InvoiceItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="invoices")
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    invoice_items = models.ManyToManyField(InvoiceItem, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Not Paid')
    
    def get_amount(self, *args, **kwargs):        
        amount = 0
        for invoice_item in self.invoice_items.all():
            amount += invoice_item.price
        return amount

    def __str__(self):
        return f'{self.patient.user.first_name} {self.patient.user.last_name} Invoice'


class Payment(models.Model):
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="payments")
    description = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)