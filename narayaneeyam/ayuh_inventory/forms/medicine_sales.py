from django import (
    forms,
)

from ayuh_inventory import (
    models,
)


class MedicineSalesForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSale
        fields = [
            "medicine",
            "quantity",
            "patient",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
