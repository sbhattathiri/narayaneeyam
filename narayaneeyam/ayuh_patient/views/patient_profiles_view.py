from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ayuh_patient import forms, models
from django.urls import reverse
from django.shortcuts import render, redirect


class PatientProfileView(CreateView):
    model = models.PatientProfile
    form_class = forms.PatientProfile
    template_name = "add_patient.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        patient_profile = form.save()
        return redirect(
            reverse("patient_profile", kwargs={"pk": patient_profile.patient_id})
        )

    def form_invalid(self, form):
        return render(self.request, "error.html", {"form": form})
