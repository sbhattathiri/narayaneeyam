from django.contrib import (
    admin,
)

from ayuh_consultation import (
    models,
)

models_to_be_registered = [models.Consultation]
admin.site.register(models_to_be_registered)
