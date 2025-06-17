import logging


from django.views.generic import (
    ListView,
)

from ayuh_facility.models.room_occupancy import RoomOccupancy

logger = logging.getLogger(__name__)


class RoomOccupancyListView(ListView):
    model = RoomOccupancy
    template_name = "ayuh_facility/list_room_occupancy_template.html"
    context_object_name = "rooms"

    def get_queryset(self):
        return RoomOccupancy.objects.select_related(
            "admission",
            "room",
            "admission__consultation",
            "admission__consultation__patient",
        ).only(
            "room__room_name",
            "room__room_category",
            "admission__consultation__patient",
            "start_date",
            "end_date",
        )
