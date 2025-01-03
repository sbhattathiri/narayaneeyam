from ayuh_patient import (
    models,
)
from crispy_forms.helper import (
    FormHelper,
)
from crispy_forms.layout import (
    Submit,
)

from django import (
    forms,
)


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Patient"))
