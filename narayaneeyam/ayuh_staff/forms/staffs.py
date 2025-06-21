from django import (
    forms,
)

from ayuh_staff import (
    models,
)


class StaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = [
            "title",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "date_of_birth",
            "designation",
            "email",
            "phone",
            "date_of_joining",
            "date_of_leaving",
        ]
        widgets = {
            "date_of_birth": forms.widgets.DateInput(attrs={"type": "date"}),
            "date_of_joining": forms.widgets.DateInput(attrs={"type": "date"}),
            "date_of_leaving": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
