from ayuh_patient import (
    views,
)

from django.urls import (
    path,
)

urlpatterns = [
    path(
        "list",
        views.PatientListView.as_view(),
        name="list_patient",
    ),
    path(
        "create/",
        views.PatientCreateView.as_view(),
        name="post_patient",
    ),
    path(
        "<uuid:pk>/update/",
        views.PatientUpdateView.as_view(),
        name="put_patient",
    ),
]
