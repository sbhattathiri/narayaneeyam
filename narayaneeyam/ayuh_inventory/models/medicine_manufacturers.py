from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineManufacturer(AyuhModel):
    name = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Medicine Manufacturer"
        verbose_name_plural = "Medicine Manufacturers"

    def __str__(self):
        return f"{self.name}"
