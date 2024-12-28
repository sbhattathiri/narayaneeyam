from ayuh_consultation import (
    models,
)

from django import (
    forms,
)

from ayuh_doctor.models import Doctor
from ayuh_patient.models import PatientProfile


class Consultation(forms.ModelForm):

    class Meta:
        model = models.Consultation
        fields = [
            "patient",
            "doctor",
            "patient_concerns",
            "diagnosis",
            "prescription",
        ]
        widgets = {
            "patient": forms.ModelChoiceField(
                queryset=PatientProfile.objects.all(),
                widget=forms.Select(
                    attrs={"id": "id_patient", "class": "select2 w-full"}
                ),
                label="Patient",
            ),
            "doctor": forms.ModelChoiceField(
                queryset=Doctor.objects.all(),
                widget=forms.Select(
                    attrs={"id": "id_doctor", "class": "select2 w-full"}
                ),
                label="Doctor",
            ),
            "patient_concerns": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "diagnosis": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "prescription": forms.TextInput(
                attrs={"class": "input input-bordered w-full"}
            ),
        }
