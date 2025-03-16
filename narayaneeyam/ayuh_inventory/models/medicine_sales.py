from django.db import (
    models,
)
from ayuh_core.models import AyuhModel
from ayuh_inventory.models.medicine_stocks import MedicineStock
from ayuh_patient.models import Patient


class MedicineSaleBatch(AyuhModel):
    sale = models.ForeignKey("MedicineSale", on_delete=models.CASCADE)
    batch = models.ForeignKey("MedicineBatch", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()


class MedicineSale(AyuhModel):
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        remaining_qty = self.quantity
        available_batches = (
            MedicineStock.objects.filter(batch__medicine=self.medicine)
            .select_related("batch")
            .order_by("batch__manufactured_date")  # FIFO logic
        )

        for stock in available_batches:
            if remaining_qty <= 0:
                break

            deducted_qty = min(remaining_qty, stock.quantity)

            # Create batch-wise sale entry
            MedicineSaleBatch.objects.create(
                sale=self, batch=stock.batch, quantity=deducted_qty
            )

            # Update stock quantity
            stock.quantity -= deducted_qty
            stock.save()

            remaining_qty -= deducted_qty

        if remaining_qty > 0:
            raise Exception(
                f"Not enough stock for {self.medicine.name} (SKU: {self.medicine.sku})"
            )
