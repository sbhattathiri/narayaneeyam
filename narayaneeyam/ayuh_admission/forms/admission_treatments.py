from ayuh_admission import (
    models,
)
from django import (
    forms,
)
from django.forms import (
    inlineformset_factory,
)


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = models.Treatment
        fields = [
            "treatment",
            "therapist",
            "treatment_date",
            "treatment_amount",
        ]
        widgets = {
            "treatment": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "therapist": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "treatment_date": forms.widgets.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "treatment_amount": forms.TextInput(
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
