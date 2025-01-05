from django.shortcuts import (
    redirect,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)

from ayuh_consultation import (
    forms,
    models,
)


class AppointmentCreateView(CreateView):
    model = models.Appointment
    form_class = forms.AppointmentForm
    template_name = "ayuh_consultation/post_appointment_template.html"
    success_url = reverse_lazy("list_consultation")
