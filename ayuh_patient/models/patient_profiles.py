import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.postgres.fields import ArrayField

from ayuh_common.ayuh_enums import BloodGroup
from ayuh_common.models import BaseModel


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
    smoking_status = models.BooleanField(null=True, blank=True)
    drinking_status = models.BooleanField(null=True, blank=True)
    substance_abuse_status = models.BooleanField(null=True, blank=True)
    dietary_preference = models.TextField(null=True, blank=True)
