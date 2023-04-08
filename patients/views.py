from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserUpdateForm
from .models import PatientProfile, Prescription
from .forms import PatientProfileForm, PrescriptionForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def patients(request):
    context = {}
    patient_profiles = PatientProfile.objects.all()

    if request.user.user_type == 'Receptionist':
        patient_profiles = PatientProfile.objects.all()
        context['patient_profiles'] = patient_profiles
    elif request.user.user_type == 'Doctor':
        patient_profiles = request.user.doctor_profile.patients.all()  
        context['patient_profiles'] = patient_profiles
    elif request.user.user_type == 'Patient':
        return redirect('accounts:home')
    
    context = {
        'patient_profiles': patient_profiles
    }

    return render(request, 'patients/patients.html', context)

@login_required()
def patient(request, id):
    patient_profile = PatientProfile.objects.get(id=id)

    context = {
        'patient_profile': patient_profile
        
    }
    return render(request, 'patients/patient.html', context)

@login_required()
def delete(request, id):
    if request.user.user_type == 'Receptionist':
        profile = PatientProfile.objects.get(id=id)
        user = profile.user
        user.delete()
        messages.success(request, 'Patient successfully deleted')
        return redirect('patients:patients')
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('patients:patients')

@login_required()
def edit(request, id):
    patient_profile = PatientProfile.objects.get(id=id)
    user = patient_profile.user

    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=user, files=request.FILES)
            profile_form = PatientProfileForm(request.POST, instance=patient_profile)
            if form.is_valid() and profile_form.is_valid():
                form.save()
                profile_form.save()
                messages.success(request, 'Changes saved')
                return redirect('patients:patient', patient_profile.id)
            messages.error(request, 'Error saving changes')
        else:
            form = UserUpdateForm(instance=user)
            profile_form = PatientProfileForm(instance=patient_profile)

        context = {
            'form': form,
            'profile_form': profile_form

        }
        return render(request, 'patients/edit.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('patients:patients')
    
@login_required()
def new(request):
    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = UserRegistrationForm(data=request.POST, files=request.FILES)
            profile_form = PatientProfileForm(data=request.POST)

            if form.is_valid() and profile_form.is_valid():
                new_user = form.save(commit=False)
                new_user.user_type = 'Patient'
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                
                new_profile = profile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.save()

                messages.success(request, "Saved successfully")
                return redirect('patients:patient', new_profile.id)
            messages.error(request, 'Form not valid')
        else:
            form = UserRegistrationForm()
            profile_form = PatientProfileForm()

        context = {
            'form': form,
            'profile_form': profile_form

        }

        return render(request, 'patients/new.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('patients:patients')

@login_required()
def prescriptions(request):
    context = {}

    if request.user.user_type == 'Receptionist':
        prescriptions = Prescription.objects.all()
        context['prescriptions'] = prescriptions
    elif request.user.user_type == 'Doctor':
        prescriptions = Prescription.objects.filter(doctor=request.user.doctor_profile) 
        context['prescriptions'] = prescriptions
    elif request.user.user_type == 'Patient':
        prescriptions = Prescription.objects.filter(patient=request.user.patient_profile) 
        context['prescriptions'] = prescriptions

    
    context = {
        'prescriptions': prescriptions
    }

    return render(request, 'patients/prescriptions/prescriptions.html', context)

@login_required()
def prescription(request, id):
    prescription = Prescription.objects.get(id=id)

    
    context = {
        'prescription': prescription
    }

    return render(request, 'patients/prescriptions/prescription.html', context)

@login_required()
def new_prescription(request):
    if request.user.user_type == 'Receptionist' or request.user.user_type == 'Doctor' :
        if request.method == 'POST':
            form = PrescriptionForm(data=request.POST, files=request.FILES)

            if form.is_valid():            
                new_prescription = form.save(commit=False)
                new_prescription.doctor = request.user.doctor_profile
                new_prescription.save()
                messages.success(request, "Saved successfully")
                return redirect('patients:prescriptions')
            messages.error(request, 'Form not valid')
        else:
            form = PrescriptionForm()

        context = {
            'form': form,
        }

        return render(request, 'patients/prescriptions/new.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('patients:patients')