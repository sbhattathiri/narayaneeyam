from crispy_forms.helper import (
    FormHelper,
)
from crispy_forms.layout import (
    Submit,
)
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
            "diagnosis",
            "doctors_comments",
            "next_consultation_date",
        ]
        widgets = {
            "consultation_date": forms.TextInput(attrs={"readonly": "readonly"}),
            "next_consultation_date": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Consultation"))
