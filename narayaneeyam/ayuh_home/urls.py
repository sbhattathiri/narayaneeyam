from django.urls import (
    path,
)

from ayuh_home import (
    views,
)


urlpatterns = [
    path("ayuh/home/", views.narayaneeyam_home, name="home"),
    path("ayuh/home/admin/", views.narayaneeyam_admin, name="admin"),
    path("ayuh/home/admission/", views.narayaneeyam_admission, name="admissions"),
]
