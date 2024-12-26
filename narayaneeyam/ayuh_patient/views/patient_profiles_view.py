from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ayuh_patient.models import Patient


class PatientProfileView(CreateView):
    model = Patient
    fields = [
        "title",
        "first_name",
        "middle_name",
        "last_name",
        "gender",
        "date_of_birth",
        "blood_type",
        "email",
        "phone",
    ]
    template_name = "add_patient.html"
    success_url = reverse_lazy("home")
