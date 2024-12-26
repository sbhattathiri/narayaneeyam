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
    path("add-patient/", views.PatientProfileView.as_view(), name="add_patient"),
]
