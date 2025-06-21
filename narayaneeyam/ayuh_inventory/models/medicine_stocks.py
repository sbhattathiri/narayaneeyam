from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineStock(AyuhModel):
    medicine = models.OneToOneField(
        "Medicine", on_delete=models.CASCADE, related_name="stock"
    )
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Medicine Stock"
        verbose_name_plural = "Medicine Stocks"

    def __str__(self):
        return f"stock for: {self.medicine} : quantity {self.quantity}"
