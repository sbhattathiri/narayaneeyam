import uuid

from ayuh_common.enums import Gender
from ayuh_common.models import BaseModel
from django.db import (
    models,
)


class Doctor(BaseModel):
    doctor_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    middle_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
    )
    gender = models.CharField(
        choices=Gender.choices(),
        null=True,
        blank=True,
        default="",
    )

    def __str__(self):
        return f"Dr. {self.last_name or ""}, {self.first_name} {self.middle_name or ""}"
