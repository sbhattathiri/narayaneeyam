from ayuh_facility.models.rooms import (
    Room,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [Room]
admin.site.register(models_to_be_registered)
