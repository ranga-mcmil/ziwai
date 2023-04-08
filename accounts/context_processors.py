from appointments.forms import AppointmentForm
from patients.forms import PrescriptionForm




def base_data(request):

    data = {}
    data["appointment_form"] = AppointmentForm()
    data["prescription_form"] = PrescriptionForm()
    return data

