from ayuh_consultation import (
    models,
)

from django.contrib import (
    admin,
)

models_to_be_registered = [models.Consultation]
admin.site.register(models_to_be_registered)
