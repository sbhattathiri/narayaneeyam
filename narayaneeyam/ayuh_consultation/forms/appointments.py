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
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
