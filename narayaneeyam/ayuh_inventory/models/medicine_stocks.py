from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineStock(AyuhModel):
    medicine = models.OneToOneField("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "medicine stock"
        verbose_name_plural = "medicine stocks"

    def __str__(self):
        return f"stock for: {self.medicine} : quantity {self.quantity}"
