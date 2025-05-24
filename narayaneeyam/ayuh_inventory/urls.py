from django.urls import (
    path,
)

from ayuh_inventory import (
    views,
)

urlpatterns = [
    path(
        "ayuh/inventory/medicine/sale/create-multiple/",
        views.MultipleMedicineSaleCreateView.as_view(),
        name="post_multiple_medicine_sale",
    ),
    path(
        "ayuh/inventory/medicine/list/",
        views.MedicineListView.as_view(),
        name="list_medicine",
    ),
    path(
        "ayuh/inventory/sale/<str:consultation_id>/prescriptions",
        views.PrescriptionsSaleView.as_view(),
        name="post_sale_of_prescriptions_for_given_consultation",
    ),
]
