import logging

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

logger = logging.getLogger(__name__)


class PatientUpdateView(UpdateView):
    model = models.PatientProfile
    slug_field = "patient_hash_id"
    form_class = forms.PatientProfileForm
    template_name = "ayuh_patient/put_patient_template.html"
    success_url = reverse_lazy("list_patient")
