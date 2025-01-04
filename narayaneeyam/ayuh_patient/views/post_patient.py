from ayuh_patient import (
    forms,
    models,
)

from django.shortcuts import (
    redirect,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)


class PatientCreateView(CreateView):
    model = models.PatientProfile
    form_class = forms.PatientForm
    template_name = "ayuh_patient/post_patient_template.html"
    success_url = reverse_lazy("list_patient")
