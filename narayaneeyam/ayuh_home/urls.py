from ayuh_home import (
    views,
)

from django.urls import (
    path,
)

urlpatterns = [
    path("", views.home, name="home_landing"),
    path("patient", views.patient_management, name="patient_management_landing"),
]
