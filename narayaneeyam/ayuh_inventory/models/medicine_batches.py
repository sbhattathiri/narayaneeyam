from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)

from ayuh_core.models import (
    AyuhModel,
)


class MedicineBatch(AyuhModel):
    batch = HashidsField(real_field_name="id")
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    manufactured_date = models.DateField(null=True, blank=True)
    shelf_life = models.PositiveSmallIntegerField(
        default=6, verbose_name="shelf life in months"
    )

    class Meta:
        verbose_name = "medicine batch"
        verbose_name_plural = "medicine batches"

    def __str__(self):
        return f"{self.batch} : {self.medicine}"
