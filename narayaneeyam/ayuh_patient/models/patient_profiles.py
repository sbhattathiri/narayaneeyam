from django.contrib.postgres.fields import (
    ArrayField,
)
from django.db import (
    models,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from ayuh_core.enums import (
    DietaryPreference,
    HabitStatus,
    Lifestyle,
)
from ayuh_patient.models.patients import (
    Patient,
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
        region="IN",
        null=True,
        blank=True,
    )
    primary_physician_email = models.EmailField(
        null=True,
        blank=True,
    )
    pre_existing_health_conditions = models.TextField(null=True, blank=True)
    pre_existing_medications = models.TextField(null=True, blank=True)
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
    smoking_status = models.CharField(
        choices=HabitStatus.choices(),
        null=True,
        blank=True,
        default="",
    )
    drinking_status = models.CharField(
        choices=HabitStatus.choices(),
        null=True,
        blank=True,
        default="",
    )
    substance_abuse_status = models.CharField(
        choices=HabitStatus.choices(),
        null=True,
        blank=True,
        default="",
    )
    dietary_preference = models.CharField(
        choices=DietaryPreference.choices(),
        null=True,
        blank=True,
        default="",
    )
    general_lifestyle = models.CharField(
        choices=Lifestyle.choices(),
        null=True,
        blank=True,
        default="",
    )
    emergency_contact_person_phone = PhoneNumberField(
        region="IN",
        null=True,
        blank=True,
    )
    patient_address = models.TextField(null=True, blank=True)

    def clean(self):
        self.primary_care_provider = (
            self.primary_care_provider.upper()
            if self.primary_care_provider
            else self.primary_care_provider
        )
        self.primary_physician_name = (
            self.primary_physician_name.upper()
            if self.primary_physician_name
            else self.primary_physician_name
        )
        self.patient_address = (
            self.patient_address.upper()
            if self.patient_address
            else self.patient_address
        )
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
