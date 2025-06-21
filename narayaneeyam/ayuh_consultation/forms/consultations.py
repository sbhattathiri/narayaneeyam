from django import (
    forms,
)

from ayuh_consultation import (
    models,
)


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = models.Consultation
        fields = [
            "patient",
            "doctor",
            "patient_concerns",
            "patient_concerns_onset_from",
            "patient_concerns_notes",
            "ongoing_medications_notes",
            "diagnosis",
            "doctor_comments",
            "doctor_notes",
            "next_consultation_date",
        ]
        widgets = {
            "patient_concerns": forms.TextInput(
                attrs={
                    "placeholder": "Capture the current concerns of the patient",
                    "class": "form-control",
                }
            ),
            "patient_concerns_onset_from": forms.TextInput(
                attrs={
                    "placeholder": "Since how long patient has been experiencing issue?",
                    "class": "form-control",
                }
            ),
            "patient_concerns_notes": forms.TextInput(
                attrs={
                    "placeholder": "Other notes from patient",
                    "class": "form-control",
                }
            ),
            "doctor_notes": forms.TextInput(
                attrs={
                    "placeholder": "Other notes from doctor",
                    "class": "form-control",
                }
            ),
            "consultation_date": forms.TextInput(
                attrs={
                    "readonly": "readonly",
                    "class": "form-control",
                }
            ),
            "next_consultation_date": forms.widgets.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
