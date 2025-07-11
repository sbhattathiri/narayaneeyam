from ayuh_admission.models.admissions import (
    Admission,
)
from ayuh_facility.models.rooms import (
    Room,
)
from django.db import (
    models,
)

from ayuh_core.models import (
    AyuhModel,
)


class RoomOccupancy(AyuhModel):
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        null=True,
        related_name="room_occupancy_admission",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="room_occupancy_room",
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Room Occupancy"
        verbose_name_plural = "Room Occupancies"
        ordering = ["-end_date"]
