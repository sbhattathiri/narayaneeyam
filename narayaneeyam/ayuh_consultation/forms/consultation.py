from django import forms

from ayuh_consultation.models import Consultation
from ayuh_doctor.models import Doctor
from ayuh_patient.models import PatientProfile


class Consultation(forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=PatientProfile.objects.all(),
        to_field_name="patient_id",
        widget=forms.Select(attrs={"id": "id_patient", "class": "select2 w-full"}),
        label="Patient",
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        to_field_name="doctor_id",
        widget=forms.Select(attrs={"id": "id_doctor", "class": "select2 w-full"}),
        label="Doctor",
    )

    patient_concerns = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Patient Concerns",
    )

    diagnosis = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Diagnosis",
    )

    prescription = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full"}),
        label="Prescription",
    )

    class Meta:
        model = Consultation
        fields = [
            "patient",
            "doctor",
            "patient_concerns",
            "diagnosis",
            "prescription",
        ]
