from django import forms
from django.forms.models import inlineformset_factory
from ayuh_inventory import (
    models,
)


class MedicineSaleForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSale
        fields = ["patient", "customer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class MedicineSaleItemsForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSaleItem
        fields = ["medicine", "quantity"]  # no patient

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


MedicineSaleItemsFormSet = inlineformset_factory(
    parent_model=models.MedicineSale,
    model=models.MedicineSaleItem,
    form=MedicineSaleItemsForm,
    extra=1,
    can_delete=True,
)
