from django.forms import (
    inlineformset_factory,
)

from ayuh_consultation import (
    models,
)

from django import forms


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = models.Prescription
        fields = ["medicine", "quantity", "instructions"]
        widgets = {
            "medicine": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "instructions": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "size": 30,
                }
            ),
        }


PrescriptionFormSet = inlineformset_factory(
    models.Consultation,
    models.Prescription,
    form=PrescriptionForm,
    extra=2,
    can_delete=True,
)
