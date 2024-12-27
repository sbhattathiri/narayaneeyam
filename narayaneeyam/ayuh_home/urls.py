from ayuh_home import (
    views,
)

from django.urls import (
    path,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("billing", views.billing_management, name="billing_management"),
    path("inventory", views.inventory_management, name="inventory_management"),
    path("patient-info", views.patient_management, name="patient_management"),
    path("reminders", views.reminders, name="reminders"),
]
