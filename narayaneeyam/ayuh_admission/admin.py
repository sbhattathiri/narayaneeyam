from ayuh_admission import (
    models,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [
    models.Admission,
    models.Treatment,
]
admin.site.register(models_to_be_registered)
