from ayuh_admission import (
    views,
)
from django.urls import (
    path,
)

urlpatterns = [
    path(
        "ayuh/admission/list/",
        views.AdmissionListView.as_view(),
        name="list_admission",
    ),
    path(
        "ayuh/admission/create/",
        views.AdmissionCreateView.as_view(),
        name="post_admission",
    ),
    path(
        "ayuh/admission/<int:pk>/",
        views.AdmissionDetailView.as_view(),
        name="get_admission",
    ),
    path(
        "ayuh/admission/<int:pk>/update/",
        views.AdmissionUpdateView.as_view(),
        name="put_admission",
    ),
]
