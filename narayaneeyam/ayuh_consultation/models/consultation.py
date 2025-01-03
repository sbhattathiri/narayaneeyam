import uuid

from ayuh_common.models import BaseModel
from django.db import (
    models,
)

from ayuh_doctor.models import Doctor
from ayuh_patient.models import PatientProfile


class Consultation(BaseModel):
    consultation_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name="consulting_patient",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="consulting_doctor",
    )
    consultation_date = models.DateTimeField(auto_now_add=True)
    patient_concerns = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    prescription = models.JSONField(null=True, blank=True, default=list)

    def __str__(self):
        return f"Consultation ID: {self.consultation_id}"
