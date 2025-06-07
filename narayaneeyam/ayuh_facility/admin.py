from django.contrib import (
    admin,
)

from ayuh_facility.models.rooms import Room

models_to_be_registered = [Room]
admin.site.register(models_to_be_registered)
