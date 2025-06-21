from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class Room(AyuhModel):
    room_name = models.CharField(null=True, blank=True)
    room_type = models.CharField(null=True, blank=True)
    room_category = models.CharField(null=True, blank=True)
    room_location = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.room_category} | {self.room_name}"
