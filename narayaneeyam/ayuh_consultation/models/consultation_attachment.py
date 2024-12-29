from ayuh_consultation.models.consultation import (
    Consultation,
)
from ayuh_core.models import (
    AyuhModel,
)

from django.db import (
    models,
)


class ConsultationAttachment(AyuhModel):
    consultation = models.ForeignKey(
        Consultation, on_delete=models.CASCADE, related_name="attachments"
    )
    attachment = models.ImageField(upload_to="consultation_attachments/")
