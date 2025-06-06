from django.db import (
    models,
)

from ayuh_core.enums import (
    MEDICINE_TYPE_CHOICES,
)
from ayuh_core.models import (
    AyuhModel,
)


class Medicine(AyuhModel):
    sku = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Stock Keeping Unit",
    )
    name = models.CharField(max_length=255)
    type = models.CharField(
        choices=MEDICINE_TYPE_CHOICES,
        null=True,
        blank=True,
        default="",
    )
    description = models.TextField(null=True, blank=True)
    manufacturer = models.ForeignKey("MedicineManufacturer", on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="price per unit",
    )

    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def __str__(self):
        return f"{self.name} ({self.sku})"
