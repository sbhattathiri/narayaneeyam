from django import (
    forms,
)

from ayuh_inventory import (
    models,
)


class MedicinesForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        fields = [
            "sku",
            "name",
            "type",
            "description",
            "manufacturer",
            "price",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
