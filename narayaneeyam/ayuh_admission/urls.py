from django.urls import (
    path,
)

from ayuh_admission import (
    views,
)

urlpatterns = [
    path(
        "ayuh/consultation/list/",
        views.AdmissionListView.as_view(),
        name="list_admission",
    ),
    path(
        "ayuh/consultation/create/",
        views.AdmissionCreateView.as_view(),
        name="post_admission",
    ),
    path(
        "ayuh/consultation/<int:pk>/",
        views.AdmissionDetailView.as_view(),
        name="get_admission",
    ),
    path(
        "ayuh/admission/<int:pk>/update/",
        views.AdmissionUpdateView.as_view(),
        name="put_admission",
    ),
]
