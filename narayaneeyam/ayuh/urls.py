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
    path(f"{settings.FACILITY_NAME}/ayuh/home/", include("ayuh_home.urls")),
    path(
        f"{settings.FACILITY_NAME}/ayuh/consultation/",
        include("ayuh_consultation.urls"),
    ),
    path(
        f"{settings.FACILITY_NAME}/ayuh/patient/",
        include("ayuh_patient.urls"),
    ),
    path(
        f"{settings.FACILITY_NAME}/ayuh/staff/",
        include("ayuh_staff.urls"),
    ),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    from debug_toolbar.toolbar import (
        debug_toolbar_urls,
    )

    urlpatterns = urlpatterns + debug_toolbar_urls()
