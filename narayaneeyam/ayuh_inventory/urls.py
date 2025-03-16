from django.urls import (
    path,
)

from ayuh_inventory import (
    views,
)

urlpatterns = [
    path(
        "/ayuh/inventory/medicine/sale/create/",
        views.MedicineSaleCreateView.as_view(),
        name="post_medicine_sale",
    ),
    path(
        "/ayuh/inventory/medicine/list/",
        views.MedicineListView.as_view(),
        name="list_medicine",
    ),
]
