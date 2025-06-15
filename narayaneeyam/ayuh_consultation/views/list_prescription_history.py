import logging

from django.db.models import (
    F,
)
from django.shortcuts import (
    get_object_or_404,
)
from django.views.generic import (
    ListView,
)

from ayuh_consultation import (
    models,
)
from ayuh_patient.models import (
    Patient,
)

logger = logging.getLogger(__name__)


class PrescriptionHistoryListView(ListView):
    model = models.Prescription
    template_name = "ayuh_consultation/list_prescription_history_template.html"
    context_object_name = "prescription_history"

    def get_queryset(self):
        self.patient = get_object_or_404(
            Patient, patient_registration_id=self.kwargs["patient_registration_id"]
        )

        prescriptions = models.Prescription.objects.filter(
            consultation__patient=self.patient
        ).select_related("consultation__doctor")
        for prescription_obj in prescriptions:
            logger.info(dir(prescription_obj))

        return prescriptions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_registration_id"] = self.patient.patient_registration_id
        context["patient_full_name"] = self.patient.full_name
        return context
