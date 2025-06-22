from ayuh_inventory import (
    models,
)
from django import (
    forms,
)
from django.forms.models import (
    inlineformset_factory,
)
from django.forms import HiddenInput


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
            "total_sale_amount",
            "total_gst_amount",
            "total_sale_amount_with_gst",
            "consultation_fee",
            "gst_on_consultation_fee",
            "total_consultation_amount_with_gst",
            "gross_amount",
            "amount_paid",
            "amount_due",
            "payment_method",
            "payment_due_date",
        ]
        labels = {
            "total_sale_amount": "Total Sale Amount",
            "total_gst_amount": "Total GST Amount",
            "total_sale_amount_with_gst": "Total Sale Amount (incl GST)",
            "consultation_fee": "Consultation Fee",
            "gst_on_consultation_fee": "GST on Consultation Fee",
            "total_consultation_amount_with_gst": "Consultation Fee (incl GST)",
            "gross_amount": "Gross Amount",
            "amount_paid": "Amount Paid",
            "amount_due": "Amount Due",
            "payment_method": "Payment Method",
            "payment_due_date": "Payment Due Date",
        }
        widgets = {
            "sale": forms.TextInput(
                attrs={"class": "form-control", "readonly": "readonly"}
            ),
            "payment_due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        readonly_fields = [
            "total_sale_amount",
            "total_gst_amount",
            "total_sale_amount_with_gst",
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
