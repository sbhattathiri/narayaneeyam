from django.contrib import (
    admin,
)

from ayuh_patient import (
    models,
)

models_to_be_registered = [models.PatientProfile]
admin.site.register(models_to_be_registered)
