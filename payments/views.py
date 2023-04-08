from django.shortcuts import render, redirect
from .forms import InvoiceForm, PaymentForm, PhoneNumberForm
from .models import Invoice, Payment
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from payments.ecocash import make_payment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def new_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(data=request.POST)

        if form.is_valid():            
            new_invoice = form.save()
            messages.success(request, "Saved successfully")
            return redirect('payments:invoice', new_invoice.id)
        messages.error(request, 'Form not valid')
    else:
        form = InvoiceForm()

    context = {
        'form': form,
    }

    return render(request, 'payments/invoices/new.html', context)

@login_required()
def invoice(request, id):
    invoice = Invoice.objects.get(id=id)

    context = {
        'invoice': invoice,
    }

    return render(request, 'payments/invoices/invoice.html', context)

@login_required()
def invoices(request):
    context = {}

    if request.user.user_type == 'Receptionist':
        invoices = Invoice.objects.all().order_by('-date_created')
        context['invoices'] = invoices
    elif request.user.user_type == 'Doctor':
        return redirect('accounts:home')
    elif request.user.user_type == 'Patient':
        invoices = Invoice.objects.filter(patient=request.user.patient_profile).order_by('-date_created')
        context['invoices'] = invoices

    return render(request, 'payments/invoices/invoices.html', context)

# PAYMENTS
@login_required()
def new(request, id):
    if request.method == 'POST':
        invoice = Invoice.objects.get(id=id)
        form = PaymentForm(data=request.POST)
        mobile_form = PhoneNumberForm(request.POST)

        if form.is_valid() and mobile_form.is_valid(): 
            phone_number = mobile_form.get_info() 
            try:
                payment_status = make_payment(f'Invoice - ID({invoice.id})', phone_number, request.user.email, 1)['status'] 
            except:
                messages.error(request, 'Something happened, make sure you are connected online')
                return redirect(request.META['HTTP_REFERER'])

            if payment_status == 'paid':
                new_payment = form.save(commit=False)
                new_payment.invoice = invoice
                new_payment.patient = invoice.patient
                new_payment.amount = invoice.get_amount()
                new_payment.save()
                invoice.status = 'Paid'
                invoice.save()
                messages.success(request, "Payment successful")
                return redirect('payments:payments')
                         
            elif payment_status == 'sent':
                messages.error(request, 'Ecocash prompt sent, could not get confirmation from user. Please try again')
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, 'Error happened, please try again')
                return redirect(request.META['HTTP_REFERER'])
 
        messages.error(request, 'Form not valid')
    else:
        form = PaymentForm()
        mobile_form = PhoneNumberForm()

    context = {
        'form': form,
        'mobile_form': mobile_form
    }

    return render(request, 'payments/new.html', context)

@login_required()
def payments(request):
    context = {}


    if request.user.user_type == 'Receptionist':
        payments = Payment.objects.all()
        context['payments'] = payments
    elif request.user.user_type == 'Doctor':
        return redirect('accounts:home')
    elif request.user.user_type == 'Patient':
        payments = Payment.objects.filter(patient=request.user.patient_profile).order_by('-date_created')
        context['payments'] = payments

    

    return render(request, 'payments/payments.html', context)