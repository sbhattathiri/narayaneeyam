from django.urls import (
    path,
)

from ayuh_patient import (
    views,
)

urlpatterns = [
    path(
        "ayuh/patient/create/",
        views.PatientCreateView.as_view(),
        name="post_patient",
    ),
    path(
        "ayuh/patient/list/",
        views.PatientListView.as_view(),
        name="list_patient",
    ),
    path(
        "ayuh/patient/<slug>/update/",
        views.PatientUpdateView.as_view(),
        name="put_patient",
    ),
]
