import uuid

from ayuh_common.enums import (
    BloodGroup,
    Gender,
    Title,
)
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
        choices=Title.choices(),
        null=True,
        blank=True,
        default="",
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
    gender = models.CharField(
        choices=Gender.choices(),
        null=True,
        blank=True,
        default="",
    )
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(
        choices=BloodGroup.choices(),
        null=True,
        blank=True,
        default="",
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
