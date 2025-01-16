import uuid

from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from ayuh_core.enums import (
    BLOOD_GROUP_CHOICES,
    Gender,
    Title,
)
from ayuh_core.models import (
    AyuhModel,
)


def generate_registration_id():
    return uuid.uuid4().hex[:10].upper()


class Patient(AyuhModel):
    patient_hash_id = HashidsField(real_field_name="id")
    patient_registration_id = models.CharField(
        max_length=10,
        unique=True,
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
        choices=BLOOD_GROUP_CHOICES,
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

    class Meta:
        unique_together = (
            "first_name",
            "middle_name",
            "last_name",
            "email",
        )

    def clean(self):
        self.first_name = (
            self.first_name.upper() if self.first_name else self.first_name
        )
        self.middle_name = (
            self.middle_name.upper() if self.middle_name else self.middle_name
        )
        self.last_name = self.last_name.upper() if self.last_name else self.last_name
        super().clean()

    def save(self, *args, **kwargs):
        if not self.patient_registration_id:
            self.patient_registration_id = generate_registration_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}  {self.first_name or ""} {self.middle_name or ""} {self.last_name or ""}"
