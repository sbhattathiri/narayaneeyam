from django.conf import (
    settings,
)
from django.contrib import (
    admin,
)
from django.urls import (
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(f"{settings.FACILITY_NAME}/admin/", admin.site.urls),
    path(f"{settings.FACILITY_NAME}/accounts/", include("django.contrib.auth.urls")),
    path(f"{settings.FACILITY_NAME}/ayuh/", include("ayuh_common.urls")),
    path(f"{settings.FACILITY_NAME}/ayuh/patients/", include("ayuh_patient.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]
