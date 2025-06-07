from django import (
    forms,
)
from django.forms import (
    inlineformset_factory,
)

from ayuh_admission import (
    models,
)


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = models.Treatment
        fields = [
            "treatment",
            "therapist",
            "treatment_date",
            "treatment_feedback",
        ]
        widgets = {
            "treatment": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "therapist": forms.ChoiceField(
                attrs={
                    "class": "form-control",
                }
            ),
            "treatment_date": forms.DateField(
                attrs={
                    "class": "form-control",
                }
            ),
            "treatment_feedback": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


TreatmentFormSet = inlineformset_factory(
    models.Admission,
    models.Treatment,
    form=TreatmentForm,
    extra=1,
    can_delete=True,
)
