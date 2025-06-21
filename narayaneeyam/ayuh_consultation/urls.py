from django.urls import (
    path,
)

from ayuh_consultation import (
    views,
)

urlpatterns = [
    path(
        "ayuh/consultation/create/",
        views.ConsultationCreateView.as_view(),
        name="post_consultation",
    ),
    path(
        "ayuh/consultation/<int:pk>/",
        views.ConsultationDetailView.as_view(),
        name="get_consultation",
    ),
    path(
        "ayuh/consultation/list/",
        views.ConsultationListView.as_view(),
        name="list_consultation",
    ),
    path(
        "ayuh/consultation/<int:pk>/update/",
        views.ConsultationUpdateView.as_view(),
        name="put_consultation",
    ),
    path(
        "ayuh/consultation/prescriptions/search",
        views.PrescriptionSearchView.as_view(),
        name="post_search_prescription_history",
    ),
    path(
        "ayuh/consultation/prescriptions/<str:patient_registration_id>/history",
        views.PrescriptionHistoryListView.as_view(),
        name="prescription_history",
    ),
]
