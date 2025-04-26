from django import forms
from django.forms import formset_factory


class PrescriptionForGivenConsultationForm(forms.Form):
    medicine = forms.CharField(disabled=True, required=False)
    sku = forms.CharField(required=False)
    quantity = forms.IntegerField(min_value=1)
    instructions = forms.CharField(disabled=True, required=False)


PrescriptionForGivenConsultationFormSet = formset_factory(
    PrescriptionForGivenConsultationForm, extra=0
)
