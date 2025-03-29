from django import (
    forms,
)
from django.forms import inlineformset_factory

from ayuh_inventory import (
    models,
)


class MedicineSalesForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSaleItem
        fields = [
            "medicine",
            "quantity",
            "patient",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class MedicineSaleItemsForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSaleItem
        fields = ["medicine", "quantity"]


MedicineSaleItemsFormSet = inlineformset_factory(
    models.MedicineSale,
    models.MedicineSaleItem,
    form=MedicineSaleItemsForm,
    extra=1,
    can_delete=True,
)
