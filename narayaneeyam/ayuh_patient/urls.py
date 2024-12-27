from ayuh_patient import (
    views,
)
from django.urls import (
    include,
    path,
)
from rest_framework.routers import (
    DefaultRouter,
)

router = DefaultRouter()
router.register(
    r"patient-profiles", views.PatientProfileAPI, basename="patient_profile"
)

urlpatterns = [
    path("", include(router.urls)),
    path("<uuid:pk>/", views.PatientProfile.as_view(), name="view_patient"),
    path("add/", views.AddPatientProfile.as_view(), name="add_patient"),
    path("<uuid:pk>/edit/", views.UpdatePatientProfile.as_view(), name="edit_patient"),
]
