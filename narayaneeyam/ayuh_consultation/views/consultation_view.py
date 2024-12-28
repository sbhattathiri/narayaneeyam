from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)

from django.urls import (
    reverse_lazy,
)

from ayuh_consultation import models, forms


class ListConsultation(ListView):
    model = models.Consultation
    template_name = "consultation_list_consultation.html"
    context_object_name = "consultations"
    paginate_by = 10

    def get_queryset(self):
        return models.Consultation.objects.all().order_by("-consultation_date")


class AddConsultation(CreateView):
    model = models.Consultation
    form_class = forms.Consultation
    template_name = "consultation_add_consultation.html"

    def form_valid(self, form):
        # Process prescription data
        prescription = []
        medicine_names = self.request.POST.getlist("medicine_name[]")
        dosages = self.request.POST.getlist("dosage[]")

        for name, dosage in zip(medicine_names, dosages):
            if name and dosage:  # Ensure no empty fields
                prescription.append({"name_of_medicine": name, "dosage": dosage})

        form.instance.prescription = prescription  # Set prescription JSON field
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("list_consultation")


class UpdateConsultation(UpdateView):
    model = models.Consultation
    form_class = forms.Consultation
    template_name = "consultation_update_consultation.html"

    def form_valid(self, form):
        prescription = []
        medicine_names = self.request.POST.getlist("medicine_name[]")
        dosages = self.request.POST.getlist("dosage[]")

        for name, dosage in zip(medicine_names, dosages):
            if name and dosage:
                prescription.append({"name_of_medicine": name, "dosage": dosage})

        form.instance.prescription = prescription
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("list_consultation")
