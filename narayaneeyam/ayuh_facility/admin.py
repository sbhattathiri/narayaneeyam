from ayuh_facility import (
    models,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [models.Room]
admin.site.register(models_to_be_registered)
