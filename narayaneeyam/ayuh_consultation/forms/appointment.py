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


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = [
            "patient",
            "doctor",
            "appointment_date",
        ]
        widgets = {
            "appointment_date": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Appointment"))
