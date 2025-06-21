from ayuh_admission.models.mixins import (
    RoomMixin,
    TreatmentMixin,
)
from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)

from ayuh_consultation.models.consultations import (
    Consultation,
)


class Admission(RoomMixin, TreatmentMixin):
    admission_hash_id = HashidsField(real_field_name="id")
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.SET_NULL,
        null=True,
        related_name="admission_consultation",
    )
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)
