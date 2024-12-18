from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend.ayuh_patient import views

router = DefaultRouter()
router.register(
    r"patient-profiles", views.PatientProfileAPI, basename="patient_profile"
)

urlpatterns = [path("", include(router.urls))]
