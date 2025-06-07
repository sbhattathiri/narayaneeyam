from django.contrib import admin

from ayuh_facility import models

models_to_be_registered = [models.Room]
admin.site.register(models_to_be_registered)
