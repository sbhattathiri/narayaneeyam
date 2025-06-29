from ayuh_admission import (
    models,
)
from django import (
    forms,
)
from django.forms import (
    inlineformset_factory,
)


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = models.Admission
        fields = [
            "consultation",
            "treatment_overview",
            "patient_notes",
            "doctor_notes",
            "room",
            "by_stander_name",
            "by_stander_contact",
            "discharge_date",
        ]
        widgets = {
            "admission_date": forms.widgets.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "patient_notes": forms.Textarea(
                attrs={
                    "placeholder": "Patient's notes",
                    "class": "form-control",
                }
            ),
            "doctor_notes": forms.Textarea(
                attrs={
                    "placeholder": "Doctor's notes",
                    "class": "form-control",
                }
            ),
            "discharge_date": forms.widgets.DateInput(
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
