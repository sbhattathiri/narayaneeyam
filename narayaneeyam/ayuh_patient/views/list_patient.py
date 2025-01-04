import logging

from ayuh_consultation.models import (
    Appointment,
    Consultation,
)
from ayuh_patient.models import (
    Patient,
)

from django.db.models import (
    Max,
    OuterRef,
    Subquery,
)
from django.views.generic import (
    ListView,
)

logger = logging.getLogger(__name__)


class PatientListView(ListView):
    model = Patient
    template_name = "ayuh_patient/list_patient_template.html"
    context_object_name = "patients"

    def get_queryset(self):
        latest_appointments = Appointment.objects.filter(
            patient=OuterRef("pk")
        ).order_by("-appointment_date")
        latest_appointment_data = latest_appointments.values(
            "doctor", "appointment_date"
        )[:1]

        patients_with_appointment = Patient.objects.annotate(
            latest_appointment_doctor_title=Subquery(
                latest_appointment_data.values("doctor__title")
            ),
            latest_appointment_doctor_first_name=Subquery(
                latest_appointment_data.values("doctor__first_name")
            ),
            latest_appointment_doctor_middle_name=Subquery(
                latest_appointment_data.values("doctor__middle_name")
            ),
            latest_appointment_doctor_last_name=Subquery(
                latest_appointment_data.values("doctor__last_name")
            ),
            latest_appointment_date=Subquery(
                latest_appointment_data.values("appointment_date")
            ),
        )

        patient_data = []
        for patient in patients_with_appointment:
            patient_data.append(
                {
                    "patient_id": patient.patient_id,
                    "patient": patient,
                    "doctor": f"{patient.latest_appointment_doctor_title or ""} "
                    f"{patient.latest_appointment_doctor_last_name or ""}"
                    f"{"," if patient.latest_appointment_doctor_last_name else ""} "
                    f"{patient.latest_appointment_doctor_first_name or ""} "
                    f"{patient.latest_appointment_doctor_middle_name or ""}",
                    "appointment_date": patient.latest_appointment_date,
                }
            )

        return patient_data
