from ayuh_inventory import (
    views,
)
from django.urls import (
    path,
)

urlpatterns = [
    path(
        "ayuh/consultation/search/",
        views.ConsultationSearchView.as_view(),
        name="post_search_consultations",
    ),
    path(
        "ayuh/inventory/medicine/list/",
        views.MedicineListView.as_view(),
        name="list_medicine",
    ),
    path(
        "ayuh/inventory/medicine/sale/",
        views.MedicineSaleCreateView.as_view(),
        name="post_medicine_sale",
    ),
    path(
        "ayuh/inventory/sale/<str:consultation_id>/prescriptions",
        views.PrescriptionsSaleView.as_view(),
        name="post_sale_of_prescriptions_for_given_consultation",
    ),
]
