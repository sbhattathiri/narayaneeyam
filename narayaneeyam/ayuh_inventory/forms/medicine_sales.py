from ayuh_inventory import (
    models,
)
from django import (
    forms,
)
from django.forms.models import (
    inlineformset_factory,
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
        fields = ["medicine", "quantity"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class MedicineSalePaymentInfoForm(forms.ModelForm):
    class Meta:
        model = models.MedicineSalePaymentInfo
        fields = [
            "sale",
            "total_amount",
            "gst",
            "gst_amount",
            "total_amount_with_gst",
            "amount_paid",
            "amount_due",
            "payment_method",
            "payment_due_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        readonly_fields = [
            "sale",
            "total_amount",
            "gst",
            "gst_amount",
            "total_amount_with_gst",
        ]
        for field in readonly_fields:
            self.fields[field].widget.attrs["readonly"] = True
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


MedicineSaleItemsFormSet = inlineformset_factory(
    parent_model=models.MedicineSale,
    model=models.MedicineSaleItem,
    form=MedicineSaleItemsForm,
    extra=1,
    can_delete=True,
)
