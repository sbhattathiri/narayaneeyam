from django.views.generic import (
    ListView,
)
from django.shortcuts import get_object_or_404
from django.db.models import F
from ayuh_consultation import (
    models,
)
from ayuh_patient.models import Patient


class PrescriptionHistoryListView(ListView):
    model = models.Prescription
    template_name = "ayuh_consultation/list_prescription_history_template.html"
    context_object_name = "prescription_history"
    paginate_by = 20

    def get_queryset(self):
        self.patient = get_object_or_404(
            Patient, patient_registration_id=self.kwargs["patient_registration_id"]
        )
        prescriptions = (
            models.Prescription.objects.filter(consultation__patient=self.patient)
            .annotate(
                consulting_id=F("consultation__appointment_hash_id"),
                consulting_date=F("consultation__consultation_date"),
                consulting_doctor=F("consultation__doctor"),
            )
            .order_by("consultation__consultation_date")
        )
        return prescriptions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_registration_id"] = self.patient
        return context
