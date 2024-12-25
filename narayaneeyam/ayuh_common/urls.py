from ayuh_common import (
    views,
)
from django.urls import (
    path,
)

urlpatterns = [
    path("billing", views.billing_info, name="billing_info"),
    path("home", views.home, name="home"),
    path("inventory", views.inventory_info, name="inventory_info"),
    path("patient-info", views.patient_info, name="patient_info"),
    path("reminders", views.reminders, name="reminders"),
]
