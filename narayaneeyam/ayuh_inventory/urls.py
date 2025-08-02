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
    path(
        "ayuh/inventory/sale/<int:pk>/payment",
        views.MedicineSalePaymentInfoCreateView.as_view(),
        name="post_payment_info",
    ),
    path(
        "ayuh/inventory/sale/<int:pk>",
        views.MedicineSaleDetailView.as_view(),
        name="get_medicine_sale",
    ),
    path(
        "ayuh/inventory/sale/<int:pk>/invoice",
        views.SaleInvoiceView.as_view(),
        name="get_sale_invoice",
    ),
]
