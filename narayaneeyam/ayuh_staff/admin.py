from ayuh_staff import (
    models,
)

from django.contrib import (
    admin,
)

models_to_be_registered = [models.Staff]
admin.site.register(models_to_be_registered)
