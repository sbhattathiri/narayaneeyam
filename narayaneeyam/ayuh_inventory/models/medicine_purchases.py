from django.db import (
    models,
)
from ayuh_core.models import AyuhModel
from ayuh_inventory.models.medicine_stocks import MedicineStock


class MedicinePurchase(AyuhModel):
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="price per unit",
    )
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Medicine Purchase"
        verbose_name_plural = "Medicine Purchases"

    def save(self, *args, **kwargs):
        medicine_stock = MedicineStock.objects.get(medicine=self.medicine)
        quantity_in_stock = medicine_stock.quantity

        medicine_stock.update(quantity=(quantity_in_stock + self.quantity))

        super(MedicinePurchase, self).save(*args, **kwargs)
