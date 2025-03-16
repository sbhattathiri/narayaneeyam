from django.db import (
    models,
)
from phonenumber_field.modelfields import (
    PhoneNumberField,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineSupplier(AyuhModel):
    supplier = models.CharField(max_length=255)
    phone = PhoneNumberField(
        region="IN",
        null=True,
        blank=True,
    )
    email = models.EmailField(blank=True, null=True)
    is_blacklisted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "medicine supplier"
        verbose_name_plural = "medicine suppliers"

    def __str__(self):
        return f"{self.email}"
