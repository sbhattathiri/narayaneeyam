from ayuh_admission.models.mixins import (
    RoomMixin,
    TreatmentMixin,
)
from django.db import (
    models,
)

from ayuh_consultation.models.consultations import (
    Consultation,
)


class Admission(RoomMixin, TreatmentMixin):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.SET_NULL,
        null=True,
        related_name="admission_consultation",
    )
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)
