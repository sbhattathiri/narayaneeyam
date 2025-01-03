from ayuh_common.enums import Title, BloodGroup, Gender
from ayuh_common.enums.ayuh_enums import HabitStatus
from ayuh_patient import models
from django import forms


class PatientProfile(forms.ModelForm):
    title = forms.ChoiceField(
        choices=Title.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        label="Title",
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="First Name",
    )

    middle_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Middle Name",
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Last Name",
    )

    gender = forms.ChoiceField(
        choices=Gender.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        label="Gender",
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Date of Birth"
    )

    blood_type = forms.ChoiceField(
        choices=BloodGroup.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        label="Blood Type",
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Email",
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Phone",
    )

    primary_care_provider = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Primary Care Provider",
    )

    primary_physician_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Primary Physician Name",
    )

    primary_physician_phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Primary Physician Phone",
    )

    primary_physician_email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Primary Physician Email",
    )

    pre_existing_health_conditions = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        required=False,
        label="Pre-existing Health Conditions",
    )

    pre_existing_medications = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        required=False,
        label="Pre-existing Medications",
    )

    known_allergies = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        required=False,
        label="Known Allergies",
    )

    known_medication_allergies = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        required=False,
        label="Known Medication Allergies",
    )

    previous_surgeries = forms.CharField(
        widget=forms.Textarea(attrs={"class": "textarea textarea-bordered w-full"}),
        required=False,
        label="Previous Surgeries",
    )

    smoking_status = forms.ChoiceField(
        choices=HabitStatus.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        required=False,
        label="Smoking Status",
    )

    drinking_status = forms.ChoiceField(
        choices=HabitStatus.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        required=False,
        label="Drinking Status",
    )

    substance_abuse_status = forms.ChoiceField(
        choices=HabitStatus.choices(),
        widget=forms.Select(attrs={"class": "select select-bordered w-full"}),
        required=False,
        label="Substance Abuse Status",
    )

    dietary_preference = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Dietary Preference",
    )

    emergency_contact_person_phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        required=False,
        label="Emergency Contact Person Phone",
    )

    class Meta:
        model = models.PatientProfile
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
