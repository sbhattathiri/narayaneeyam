from django.urls import (
    path,
)

from ayuh_facility import (
    views,
)

urlpatterns = [
    path(
        "ayuh/facility/room-occupancy/list/",
        views.RoomOccupancyListView.as_view(),
        name="list_room_occupancy",
    ),
]
