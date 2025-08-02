from django.db import (
    models,
)

from ayuh_consultation.models.appointments import (
    Appointment,
)
from ayuh_consultation.managers import ConsultationManager


class Consultation(Appointment):
    # Add optimized manager
    objects = ConsultationManager()
    
    consultation_date = models.DateTimeField(auto_now_add=True)
    patient_concerns = models.TextField(null=True, blank=True)
    patient_concerns_onset_from = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    patient_concerns_notes = models.TextField(null=True, blank=True)
    ongoing_medications_notes = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    doctor_comments = models.TextField(null=True, blank=True)
    doctor_notes = models.TextField(null=True, blank=True)
    next_consultation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        patient_name = (
            f"{self.patient.title or ""} {self.patient.last_name or ""}"
            if self.patient
            else "Unknown"
        )
        doctor_name = f"Dr. {self.doctor.last_name or ""}" if self.doctor else "Unknown"
        return f"Patient: {patient_name} consulted {doctor_name} on {self.appointment_date}"
