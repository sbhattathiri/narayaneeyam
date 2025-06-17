from ayuh_facility.models.room_occupancy import RoomOccupancy
from ayuh_facility.models.rooms import (
    Room,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [Room, RoomOccupancy]
admin.site.register(models_to_be_registered)
