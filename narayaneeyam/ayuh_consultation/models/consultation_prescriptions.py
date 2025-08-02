from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)

from ayuh_consultation.models.consultations import (
    Consultation,
)
from ayuh_core.models import (
    AyuhModel,
)
from ayuh_consultation.managers import PrescriptionManager


class Prescription(AyuhModel):
    # Add optimized manager
    objects = PrescriptionManager()
    
    prescription_hash_id = HashidsField(real_field_name="id")
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name="consultation_prescription",
    )
    medicine = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
