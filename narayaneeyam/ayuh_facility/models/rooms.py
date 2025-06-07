from ayuh_core.models import AyuhModel
from django.db import (
    models,
)


class Room(AyuhModel):
    room_name = models.CharField(null=True, blank=True)
    room_type = models.CharField(null=True, blank=True)
    room_category = models.CharField(null=True, blank=True)
    room_location = models.DateField(null=True, blank=True)
