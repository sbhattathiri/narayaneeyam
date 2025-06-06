import logging

from ayuh_inventory import (
    models,
)
from django import (
    forms,
)

logger = logging.getLogger(__name__)


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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({"class": "form-control"})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     if self.instance:
    #         logger.info(f"instance exists")
    #         medicine_batch = self.instance.medicinebatch_set.filter(
    #             medicinestock__isnull=False
    #         ).first()
    #
    #         if medicine_batch and hasattr(medicine_batch, "medicinestock"):
    #             logger.info("medicine_batch exists, and hasattr medicinestock")
    #             medicine_stock = getattr(medicine_batch, "medicinestock", None)
    #             if medicine_stock:
    #                 self.fields["stock"].initial = medicine_stock.stock
    #             else:
    #                 self.fields["stock"].initial = "N/A"
    #         else:
    #             self.fields["stock"].initial = "N/A"
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({"class": "form-control"})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        logger.info(f"instance exists")
        medicine_batch = self.instance.medicinebatch_set.filter(
            medicinestock__isnull=False
        ).first()

        if medicine_batch and hasattr(medicine_batch, "medicinestock"):
            logger.info("medicine_batch exists, and hasattr medicinestock")
            medicine_stock = getattr(medicine_batch, "medicinestock", None)
            if medicine_stock:
                self.fields["stock"].initial = medicine_stock.stock
            else:
                self.fields["stock"].initial = "N/A"
        else:
            self.fields["stock"].initial = "N/A"

        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
