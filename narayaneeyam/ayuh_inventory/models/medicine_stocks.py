from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineStock(AyuhModel):
    batch = models.OneToOneField("MedicineBatch", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "medicine stock"
        verbose_name_plural = "medicine stocks"
