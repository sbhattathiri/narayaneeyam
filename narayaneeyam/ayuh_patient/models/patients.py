import uuid

from ayuh_common.models import (
    BaseModel,
)
from django.db import (
    models,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)


class Patient(BaseModel):
    patient_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    title = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    middle_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone = PhoneNumberField(
        region="IN",
        null=True,
        blank=True,
    )
    emergency_contact_person_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    emergency_contact_person_phone = PhoneNumberField(
        region="IN",
        null=True,
        blank=True,
    )
