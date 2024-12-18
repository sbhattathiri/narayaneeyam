from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings


urlpatterns = [
    path(f"{settings.FACILITY_NAME}/admin/", admin.site.urls),
    path(f"{settings.FACILITY_NAME}/accounts/", include("django.contrib.auth.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_patient.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]
