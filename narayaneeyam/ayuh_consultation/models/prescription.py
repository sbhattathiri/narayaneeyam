import uuid

from django.db import (
    models,
)

from ayuh_consultation.models.consultation import (
    Consultation,
)
from ayuh_core.models import (
    AyuhModel,
)


class Prescription(AyuhModel):
    prescription_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name="consulting_patient",
    )
    medicine = models.CharField(max_length=255)
    instructions = models.TextField(null=True, blank=True)
