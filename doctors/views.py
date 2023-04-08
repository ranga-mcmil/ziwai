from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserUpdateForm
from .models import DoctorProfile
from .forms import DoctorProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def doctors(request):
    context = {}

    if request.user.user_type == 'Receptionist':
        doctor_profiles = DoctorProfile.objects.all()
        context['doctor_profiles'] = doctor_profiles
    elif request.user.user_type == 'Doctor':
        return redirect('accounts:home')
    elif request.user.user_type == 'Patient':
        doctor_profile = request.user.patient_profile.doctor   
        context['doctor_profile'] = doctor_profile

    return render(request, 'doctors/doctors.html', context)

@login_required()
def doctor(request, id):
    doctor_profile = DoctorProfile.objects.get(id=id)

    context = {
        'doctor_profile': doctor_profile
        
    }
    return render(request, 'doctors/doctor.html', context)

def delete(request, id):
    if request.user.user_type == 'Receptionist':
        profile = DoctorProfile.objects.get(id=id)
        user = profile.user
        user.delete()
        messages.success(request, 'Doctor successfully deleted')
        return redirect('doctors:doctors')
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('doctors:doctors')



# TODO
@login_required()
def edit(request, id):
    doctor_profile = DoctorProfile.objects.get(id=id)
    user = doctor_profile.user

    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=user, files=request.FILES)
            profile_form = DoctorProfileForm(request.POST, instance=doctor_profile)
            if form.is_valid() and profile_form.is_valid():
                form.save()
                profile_form.save()
                messages.success(request, 'Changes saved')
                return redirect('doctors:doctor', doctor_profile.id)
            messages.error(request, 'Error saving changes')
        else:
            form = UserUpdateForm(instance=user)
            profile_form = DoctorProfileForm(instance=doctor_profile)

        context = {
            'form': form,
            'profile_form': profile_form

        }
        return render(request, 'doctors/edit.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('doctors:doctors')
    
@login_required()
def new(request):
    if request.user.user_type == 'Receptionist':
        if request.method == 'POST':
            form = UserRegistrationForm(data=request.POST, files=request.FILES)
            profile_form = DoctorProfileForm(data=request.POST)

            if form.is_valid() and profile_form.is_valid():
                new_user = form.save(commit=False)
                new_user.user_type = 'Doctor'
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                
                new_profile = profile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.save()

                messages.success(request, "Saved successfully")
                return redirect('doctors:doctor', new_profile.id)
            messages.error(request, 'Form not valid')
        else:
            form = UserRegistrationForm()
            profile_form = DoctorProfileForm()

        context = {
            'form': form,
            'profile_form': profile_form

        }
        return render(request, 'doctors/new.html', context)
    else:
        messages.error(request, 'You do not have rights to perform this action')
        return redirect('doctors:doctors')

