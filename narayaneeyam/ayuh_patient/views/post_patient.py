from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)

from ayuh_patient import (
    forms,
    models,
)


class PatientCreateView(CreateView):
    model = models.PatientProfile
    form_class = forms.PatientForm
    template_name = "ayuh_patient/post_patient_template.html"
    success_url = reverse_lazy("list_patient")
