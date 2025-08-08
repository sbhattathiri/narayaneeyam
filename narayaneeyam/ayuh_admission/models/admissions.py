from ayuh import (
    settings,
)
from ayuh_facility.models.rooms import (
    Room,
)

# from ayuh_admission.models.mixins import (
#     RoomMixin,
#     TreatmentMixin,
# )
from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from ayuh_consultation.models.consultations import (
    Consultation,
)
from ayuh_core.models import (
    AyuhModel,
)
from ayuh_admission.managers import AdmissionManager


class Admission(AyuhModel):
    # Add optimized manager
    objects = AdmissionManager()
    
    admission_hash_id = HashidsField(real_field_name="id")
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.SET_NULL,
        null=True,
        related_name="admission_consultation",
    )
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(null=True, blank=True)

    treatment_overview = models.TextField(null=True, blank=True)
    patient_notes = models.TextField(null=True, blank=True)
    doctor_notes = models.TextField(null=True, blank=True)
    treatment_updated_at = models.DateTimeField(auto_now=True)
    treatment_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    by_stander_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    by_stander_contact = PhoneNumberField(
        region="IN",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.admission_hash_id} | {self.consultation.patient}"
