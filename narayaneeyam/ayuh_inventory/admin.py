from ayuh_inventory import (
    models,
)
from django.contrib import (
    admin,
)

models_to_be_registered = [
    models.MedicineManufacturer,
    models.MedicinePurchase,
    models.MedicineStock,
    models.Medicine,
]
admin.site.register(models_to_be_registered)
