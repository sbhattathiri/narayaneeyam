from ayuh import (
    settings,
)
from ayuh_facility.models.rooms import (
    Room,
)
from django.db import (
    models,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)


class TreatmentMixin(models.Model):
    treatment_overview = models.TextField(null=True, blank=True)
    patient_notes = models.TextField(null=True, blank=True)
    doctor_notes = models.TextField(null=True, blank=True)
    treatment_updated_at = models.DateTimeField(auto_now=True)
    treatment_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by",
        help_text="the user who last updated this record.",
    )

    class Meta:
        abstract = True


class RoomMixin(models.Model):
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

    class Meta:
        abstract = True
