from ayuh_inventory.models import (
    Medicine,
)
from django import (
    forms,
)
from django.forms import (
    formset_factory,
)


class PrescriptionForGivenConsultationForm(forms.Form):
    medicine = forms.CharField(disabled=True, required=False)
    sku = forms.ModelChoiceField(
        queryset=Medicine.objects.all(),
        required=False,
        label="SKU",
    )
    quantity = forms.IntegerField(min_value=1)
    instructions = forms.CharField(disabled=True, required=False)


PrescriptionForGivenConsultationFormSet = formset_factory(
    PrescriptionForGivenConsultationForm, extra=0
)
