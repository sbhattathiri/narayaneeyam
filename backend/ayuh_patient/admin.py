from django.contrib import admin
from backend.ayuh_patient import models

models_to_be_registered = [models.PatientProfile, models.PatientAddress]
admin.site.register(models_to_be_registered)
