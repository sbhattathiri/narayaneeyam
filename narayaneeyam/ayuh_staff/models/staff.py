import uuid

from ayuh_core.enums import (
    Gender,
    StaffRole,
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


class Staff(AyuhModel):
    staff_id = models.UUIDField(
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
    date_of_birth = models.DateField(null=True, blank=True)
    designation = models.CharField(
        choices=StaffRole.choices(),
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
    date_of_joining = models.DateField(null=True, blank=True)
    date_of_leaving = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            "first_name",
            "middle_name",
            "last_name",
            "email",
        )

    def __str__(self):
        return f"{self.title or ""} {self.last_name or ""}, {self.first_name} {self.middle_name or ""}"
