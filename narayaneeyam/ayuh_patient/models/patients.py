import uuid

from ayuh_core.enums import (
    BloodGroup,
    Gender,
    Title,
)
from ayuh_core.models import (
    AyuhModel,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from django.db import (
    models,
)


class Patient(AyuhModel):
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

    def __str__(self):
        return f"{self.title} {self.last_name}, {self.first_name} {self.middle_name}"
