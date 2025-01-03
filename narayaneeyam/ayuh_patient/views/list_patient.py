import logging

from django.db.models import Max
from ayuh_consultation.models import Consultation

from django.views.generic import (
    ListView,
)

from ayuh_patient.models import Patient

logger = logging.getLogger(__name__)


class PatientListView(ListView):
    model = Patient
    template_name = "ayuh_patient/list_patient_template.html"
    context_object_name = "patients"

    def get_queryset(self):
        consultations = Consultation.objects.values("patient").annotate(
            last_consultation_date=Max("consultation_date")
        )
        logger.info(f"consultations: {consultations}")

        patient_data = []
        for consultation in consultations:
            patient = Patient.objects.get(patient_id=consultation["patient"])
            last_consultation = (
                patient.consulting_patient.filter(
                    consultation_date=consultation["last_consultation_date"]
                ).first()
                if consultation["last_consultation_date"]
                else None
            )
            doctor = last_consultation.doctor if last_consultation else None
            last_consultation_date = (
                consultation["last_consultation_date"] if last_consultation else None
            )
            patient_data.append(
                {
                    "patient_id": consultation["patient"],
                    "patient": patient,
                    "doctor": doctor,
                    "last_consultation_date": last_consultation_date,
                }
            )

        logger.info(f"consulting patients: {patient_data}")
        patients_without_consultations = Patient.objects.filter(
            consulting_patient__isnull=True
        )
        for patient in patients_without_consultations:
            patient_data.append(
                {
                    "patient_id": patient.patient_id,
                    "patient": patient,
                    "doctor": None,
                    "last_consultation_date": None,
                }
            )

        logger.info(f"patients: {patient_data}")
        return patient_data
