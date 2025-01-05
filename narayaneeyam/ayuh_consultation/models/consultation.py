from django.db import (
    models,
)

from ayuh_consultation.models.appointment import (
    Appointment,
)


class Consultation(Appointment):
    consultation_date = models.DateTimeField(auto_now_add=True)
    patient_concerns = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    doctors_comments = models.TextField(null=True, blank=True)
    next_consultation_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        patient_name = (
            f"{self.patient.title or ""} {self.patient.last_name or ""}"
            if self.patient
            else "Unknown"
        )
        doctor_name = f"Dr. {self.doctor.last_name or ""}" if self.doctor else "Unknown"
        return f"Patient: {patient_name} consulted {doctor_name} on {self.appointment_date}"
