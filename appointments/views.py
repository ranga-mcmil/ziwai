from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required()
def appointments(request):

    if request.user.user_type == 'Receptionist':
        appointments = Appointment.objects.all()
    elif request.user.user_type == 'Doctor':
        appointments = Appointment.objects.filter(doctor=request.user.doctor_profile)
    elif request.user.user_type == 'Patient':
        appointments = Appointment.objects.filter(patient=request.user.patient_profile)

    context = {
        'appointments': appointments
    }

    return render(request, 'appointments/appointments.html', context)


@login_required()
def appointment(request, id):
    appointment = Appointment.objects.get(id=id)

    context = {
        'appointment': appointment
        
    }
    return render(request, 'appointments/appointment.html', context)

@login_required()
def new(request):
    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = AppointmentForm(data=request.POST, files=request.FILES)

            if form.is_valid():
                new_appointment = form.save()
                messages.success(request, "Saved successfully")
                return redirect('appointments:appointments')
            messages.error(request, 'Form not valid')
        else:
            form = AppointmentForm()
        context = {
            'form': form,
        }

        return render(request, 'appointments/new.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('appointments:appointments')

@login_required()
def edit(request, id):
    appointment = Appointment.objects.get(id=id)

    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Changes saved')
                return redirect('appointments:appointments')
            messages.error(request, 'Error saving changes')
        else:
            form = AppointmentForm(instance=appointment)

        context = {
            'form': form,
        }
        return render(request, 'appointments/edit.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('appointments:appointments')

@login_required()
def delete(request, id):
    if request.user.user_type == 'Receptionist':
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        messages.success(request, 'Appointment successfully deleted')
        return redirect('appointments:appointments')
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('appointments:appointments')