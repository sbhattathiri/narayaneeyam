from ayuh_patient import (
    views,
)
from rest_framework.routers import (
    DefaultRouter,
)

from django.urls import (
    include,
    path,
)

router = DefaultRouter()
router.register(
    r"patient-profiles", views.PatientProfileAPI, basename="patient_profile"
)

urlpatterns = [
    path("", include(router.urls)),
    path("<uuid:pk>/", views.PatientProfile.as_view(), name="view_patient"),
    path("add/", views.AddPatientProfile.as_view(), name="add_patient"),
    path(
        "<uuid:pk>/update/", views.UpdatePatientProfile.as_view(), name="update_patient"
    ),
]
