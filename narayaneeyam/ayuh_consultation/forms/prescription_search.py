from django import forms


class PrescriptionSearchForm(forms.Form):
    patient_registration_id = forms.CharField(label="Patient Registration ID")
