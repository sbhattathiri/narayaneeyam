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
        verbose_name = "medicine manufacturer"
        verbose_name_plural = "medicine manufacturers"

    def __str__(self):
        return f"{self.name}"
