from ayuh_patient import views, models
from django.urls import (
    include,
    path,
)
from rest_framework.routers import (
    DefaultRouter,
)
from django.views.generic.detail import DetailView

router = DefaultRouter()
router.register(
    r"patient-profiles", views.PatientProfileAPI, basename="patient_profile"
)

urlpatterns = [
    path("", include(router.urls)),
    path("patient/add/", views.PatientProfileView.as_view(), name="add_patient"),
    path(
        "patient/<uuid:pk>/",
        DetailView.as_view(
            model=models.PatientProfile, template_name="patient_profile.html"
        ),
        name="patient_profile",
    ),
]
