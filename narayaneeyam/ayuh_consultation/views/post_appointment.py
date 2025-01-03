from ayuh_consultation import (
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


class AppointmentCreateView(CreateView):
    model = models.Consultation
    form_class = forms.ConsultationForm
    template_name = "ayuh_consultation/post_appointment_template.html"
    success_url = reverse_lazy("list_consultation")
