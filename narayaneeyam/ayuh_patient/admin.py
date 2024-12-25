from ayuh_patient import (
    models,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [models.PatientProfile, models.PatientAddress]
admin.site.register(models_to_be_registered)
