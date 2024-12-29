from ayuh_core.models.mixins import (
    TimestampedModelMixin,
    UserStampedModelMixin,
)

from django.db import (
    models,
)


class AyuhModel(
    TimestampedModelMixin,
    UserStampedModelMixin,
    models.Model,
):
    class Meta:
        abstract = True
        default_permissions = (
            "add",
            "change",
            "delete",
            "view",
            "bulk_change",
            "bulk_delete",
            "bulk_add",
            "export",
        )