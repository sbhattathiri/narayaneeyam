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

    class Meta:
        verbose_name = "Medicine Sale"
        verbose_name_plural = "Medicine Sales"


class MedicineSaleItem(AyuhModel):
    sale = models.ForeignKey(
        "MedicineSale", on_delete=models.CASCADE, related_name="items"
    )
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.sale} of {self.medicine} : {self.quantity} units"

    class Meta:
        verbose_name = "Medicine Sale Item"
        verbose_name_plural = "Medicine Sale Items"

    def save(self, *args, **kwargs):
        medicine_stock = MedicineStock.objects.get(medicine=self.medicine)
        quantity_in_stock = medicine_stock.quantity

        if quantity_in_stock <= 0:
            raise Exception(
                f"Not enough stock for {self.medicine.name} (SKU: {self.medicine.sku})"
            )

        if self.quantity > quantity_in_stock:
            self.quantity = quantity_in_stock

        medicine_stock.update(quantity=(quantity_in_stock - self.quantity))

        super(MedicineSaleItem, self).save(*args, **kwargs)
