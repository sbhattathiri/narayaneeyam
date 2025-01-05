from django.urls import (
    path,
)

from ayuh_home import (
    views,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("admin", views.admin, name="admin"),
    path("patient", views.patient, name="patients"),
    path("consultation", views.consultation, name="consultations"),
    path("admission", views.admission, name="admissions"),
    path("inventory", views.inventory, name="inventory"),
]
