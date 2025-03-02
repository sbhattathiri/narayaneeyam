from django.contrib import (
    admin,
)

from ayuh_staff import (
    models,
)

models_to_be_registered = [models.Staff]
admin.site.register(models_to_be_registered)
