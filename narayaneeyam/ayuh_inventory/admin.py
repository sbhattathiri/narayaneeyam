from django.contrib import (
    admin,
)

from ayuh_inventory import (
    models,
)

models_to_be_registered = [
    models.MedicineBatch,
    models.MedicineManufacturer,
    models.MedicinePurchase,
    models.MedicineStock,
    models.MedicineSupplier,
]
admin.site.register(models_to_be_registered)
