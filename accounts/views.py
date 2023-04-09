from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from .forms import MyPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from patients.models import PatientProfile, Prescription
from doctors.models import DoctorProfile
from payments.models import Payment
from .forms import UserRegistrationForm

# Create your views here.
@login_required()
def home(request):
    appointments = Appointment.objects.all().count
    patients = PatientProfile.objects.all().count
    doctors = DoctorProfile.objects.all().count
    payments = Payment.objects.all().count
    prescriptions = []

    if request.user.user_type == 'Doctor':
        appointments = Appointment.objects.filter(doctor=request.user.doctor_profile).count
        prescriptions = Prescription.objects.filter(doctor=request.user.doctor_profile).count
        patients = request.user.doctor_profile.patients.all().count
    elif request.user.user_type == 'Patient':
        doctors = 1
        appointments = Appointment.objects.filter(patient=request.user.patient_profile).count
        prescriptions = Prescription.objects.filter(patient=request.user.patient_profile).count
    
    context = {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors,
        'payments': payments,
        'prescriptions': prescriptions,
    }
    
    return render(request, 'accounts/home.html', context)


class PasswordChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = "registration/password_change_form.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Password updated successfully")
        return super(PasswordChangeView, self).form_valid(form)

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('About to login')
            if user.last_login == None:
                login(request, user)
                return redirect('accounts:password_change')
            else:
                login(request, user)
                messages.success(request, f'You are now logged in as {user.get_full_name()}')
                return redirect('accounts:home')
        else:
            pass
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_type = 'Receptionist'
            user.save()
            login(request, user)
            messages.success(request, f'You are now logged in as {user.get_full_name()}')
            return redirect('accounts:home')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



def my_logout(request):
    logout(request)
    messages.success(request, "You have successfully signed out")
    return redirect('accounts:home')




