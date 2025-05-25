from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)
from ayuh_core.models import AyuhModel
from ayuh_inventory.models.medicine_stocks import MedicineStock
from ayuh_patient.models import Patient


class MedicineSale(AyuhModel):
    sale_id = HashidsField(real_field_name="id")
    sale_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    customer = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Medicine Sale"
        verbose_name_plural = "Medicine Sales"


class MedicineSaleItem(AyuhModel):
    sale = models.ForeignKey(
        "MedicineSale", on_delete=models.CASCADE, related_name="items"
    )
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sale} of {self.medicine} : {self.quantity} units"

    class Meta:
        verbose_name = "Medicine Sale Item"
        verbose_name_plural = "Medicine Sale Items"
