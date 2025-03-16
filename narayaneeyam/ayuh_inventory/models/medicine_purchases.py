from django.db import (
    models,
)
from ayuh_core.models import AyuhModel


class MedicinePurchase(AyuhModel):
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    batch = models.ForeignKey("MedicineBatch", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="price per unit",
    )
    purchased_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(
        "MedicineSupplier",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "medicine purchase"
        verbose_name_plural = "medicine purchases"
