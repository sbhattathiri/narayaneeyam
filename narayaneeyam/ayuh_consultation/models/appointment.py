import uuid

from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)

from ayuh_core.enums import (
    StaffRole,
)
from ayuh_core.models import (
    AyuhModel,
)
from ayuh_patient.models import (
    Patient,
)
from ayuh_staff.models import (
    Staff,
)


class Appointment(AyuhModel):
    appointment_hash_id = HashidsField(real_field_name="id")
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="consulting_patient",
    )
    doctor = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        limit_choices_to={"designation": StaffRole.DOCTOR.value},
        db_column="doctor",
        null=True,
        blank=True,
        related_name="consulting_doctor",
    )
    appointment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        patient_name = (
            f"{self.patient.title or ""} {self.patient.last_name or ""}"
            if self.patient
            else "Unknown"
        )
        doctor_name = f"Dr. {self.doctor.last_name or ""}" if self.doctor else "Unknown"
        return f"Patient: {patient_name} booked appointment with {doctor_name} on {self.appointment_date}"
