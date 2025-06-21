from django import (
    forms,
)


class ConsultationSearchForm(forms.Form):
    consultation_id = forms.CharField(label="Consultation ID")
