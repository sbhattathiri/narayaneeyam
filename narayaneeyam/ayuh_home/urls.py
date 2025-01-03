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
    path("patient", views.patient_management, name="patient_management"),
    path("hr", views.human_resource_management, name="human_resource_management"),
    path("expense", views.expense_management, name="expense_management"),
    path("publicity", views.expense_management, name="publicity_management"),
    path("reminders", views.reminders, name="reminders"),
]
