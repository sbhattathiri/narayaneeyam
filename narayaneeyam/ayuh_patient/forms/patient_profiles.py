from django import forms

from ayuh_patient.models import PatientProfile


class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
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
            "pre_existing_medications",
            "known_allergies",
            "known_medication_allergies",
            "previous_surgeries",
            "smoking_status",
            "drinking_status",
            "substance_abuse_status",
            "dietary_preference",
            "emergency_contact_person_phone",
        ]
        widgets = {
            "title": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "first_name": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "middle_name": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "gender": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "input input-bordered w-full"}
            ),
            "blood_type": forms.Select(
                attrs={"class": "select select-bordered w-full"}
            ),
            "email": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "phone": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        }
