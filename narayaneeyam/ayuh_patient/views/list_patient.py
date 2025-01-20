import logging

from django.db.models import (
    F,
    OuterRef,
    Subquery,
    Value,
)
from django.db.models.functions import (
    Coalesce,
    Concat,
)
from django.views.generic import (
    ListView,
)

from ayuh_consultation.models import (
    Appointment,
)
from ayuh_patient.models import (
    Patient,
    PatientProfile,
)

logger = logging.getLogger(__name__)


class PatientListView(ListView):
    model = PatientProfile
    template_name = "ayuh_patient/list_patient_template.html"
    context_object_name = "patients"
    slug_field = "patient_hash_id"

    def get_queryset(self):
        latest_appointments = Appointment.objects.filter(
            patient=OuterRef("pk")
        ).order_by("-appointment_date")

        latest_appointment_data = latest_appointments.annotate(
            doctor_full_name=Concat(
                Coalesce(F("doctor__title"), Value("")),
                Value(" "),
                Coalesce(F("doctor__first_name"), Value("")),
                Value(" "),
                Coalesce(F("doctor__middle_name"), Value("")),
                Value(" "),
                Coalesce(F("doctor__last_name"), Value("")),
            )
        ).values("doctor_full_name", "appointment_date")[:1]

        patients_with_appointment = PatientProfile.objects.annotate(
            latest_appointment_doctor_full_name=Subquery(
                latest_appointment_data.values("doctor_full_name")
            ),
            latest_appointment_date=Subquery(
                latest_appointment_data.values("appointment_date")
            ),
        )

        patient_data = []
        for patient in patients_with_appointment:
            patient_data.append(
                {
                    "patient_hash_id": patient.patient_hash_id,
                    "patient": patient,
                    "doctor": patient.latest_appointment_doctor_full_name,
                    "appointment_date": patient.latest_appointment_date,
                }
            )

        return patient_data
