from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    UpdateView,
)

from ayuh_patient import (
    forms,
    models,
)


class PatientUpdateView(UpdateView):
    model = models.Patient
    form_class = forms.PatientForm
    template_name = "ayuh_patient/put_patient_template.html"
    success_url = reverse_lazy("list_patient")
