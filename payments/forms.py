from django import forms
from .models import Invoice, Payment, InvoiceItem
from patients.models import PatientProfile

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'val',
            'id': 'search-input01',

        }
    ))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()
        phone_number = cl_data.get('phone_number')
        return phone_number


class InvoiceForm(forms.ModelForm):

    patient = forms.ModelChoiceField(queryset=PatientProfile.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    invoice_items = forms.ModelMultipleChoiceField(
        required=False,
        queryset=InvoiceItem.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs = {
            'class': '',
        }),
    )

    class Meta:
        model = Invoice
        fields = ('patient', 'invoice_items', 'due_date')
        widgets = {
            'due_date': forms.TextInput(
                attrs={'type': 'datetime-local'}
            )
        }



class PaymentForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'description',
        }
    ))

    class Meta:
        model = Payment
        fields = ('description',)