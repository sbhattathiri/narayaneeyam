from ayuh_doctor import (
    models,
)

from django.contrib import (
    admin,
)

models_to_be_registered = [models.Doctor]
admin.site.register(models_to_be_registered)
