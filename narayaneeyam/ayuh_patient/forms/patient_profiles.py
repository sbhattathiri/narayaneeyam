from django import (
    forms,
)
from django.forms import (
    ModelForm,
)

from ayuh_patient.models import (
    PatientProfile,
)


class PatientProfileForm(ModelForm):

    class Meta:
        model = PatientProfile
        fields = [
            "patient_registration_id",
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "date_of_birth",
            "blood_type",
            "email",
            "phone",
            "primary_care_provider",
            "primary_physician_name",
            "primary_physician_phone",
            "primary_physician_email",
            "pre_existing_health_conditions",
            "known_allergies",
            "known_medication_allergies",
            "previous_surgeries",
            "smoking_status",
            "drinking_status",
            "substance_abuse_status",
            "dietary_preference",
            "general_lifestyle",
            "emergency_contact_person_phone",
            "patient_address",
        ]

        widgets = {
            "patient_registration_id": forms.widgets.TextInput(
                attrs={"readonly": True}
            ),
            "date_of_birth": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
