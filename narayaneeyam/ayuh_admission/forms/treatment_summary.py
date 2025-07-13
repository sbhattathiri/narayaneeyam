# from django import (
#     forms,
# )
#
#
# class TreatmentSummaryForm(forms.Form):
#     treatment_id = forms.IntegerField(widget=forms.HiddenInput())
#     treatment = forms.CharField(disabled=True)
#     therapist = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}), disabled=True)
#     treatment_date = forms.DateField(disabled=True)
#     cost = forms.DecimalField(required=True, min_value=0)
