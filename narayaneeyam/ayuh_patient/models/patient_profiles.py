from ayuh_common.enums import (
    BloodGroup,
)
from ayuh_patient.models.patients import (
    Patient,
)
from django.contrib.postgres.fields import (
    ArrayField,
)
from django.db import (
    models,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)


class PatientProfile(Patient):
    primary_care_provider = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_comment="Name of the Clinic/Hospital which the patient goes to",
    )
    primary_physician_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    primary_physician_phone = PhoneNumberField(
        null=True,
        blank=True,
    )
    primary_physician_email = models.EmailField(
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(
        choices=BloodGroup.choices(),
        null=True,
        blank=True,
        default="",
    )
    known_allergies = ArrayField(
        models.CharField(max_length=255),
        null=True,
        blank=True,
    )
    known_medication_allergies = ArrayField(
        models.CharField(max_length=255),
        null=True,
        blank=True,
    )
    previous_surgeries = ArrayField(
        models.CharField(max_length=255),
        null=True,
        blank=True,
    )
    pre_existing_medications = models.TextField(null=True, blank=True)
    pre_existing_health_conditions = models.TextField(null=True, blank=True)
    smoking_status = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )
    drinking_status = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )
    substance_abuse_status = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )
    dietary_preference = models.TextField(null=True, blank=True)
