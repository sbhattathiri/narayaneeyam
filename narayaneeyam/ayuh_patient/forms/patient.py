from django import (
    forms,
)

from ayuh_patient import (
    models,
)


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.PatientProfile
        fields = [
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "date_of_birth",
            "blood_type",
            "email",
            "phone",
        ]
        widgets = {
            "date_of_birth": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
