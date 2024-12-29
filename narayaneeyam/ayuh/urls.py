from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

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

urlpatterns = [
    path(f"{settings.FACILITY_NAME}/admin/", admin.site.urls),
    path(f"{settings.FACILITY_NAME}/accounts/", include("django.contrib.auth.urls")),
    path(f"{settings.FACILITY_NAME}/ayuh/home/", include("ayuh_home.urls")),
    path(
        f"{settings.FACILITY_NAME}/ayuh/consultation/",
        include("ayuh_consultation.urls"),
    ),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

if not settings.TESTING:
    import debug_toolbar

    urlpatterns = [
        *urlpatterns,
        path("debug/", include(debug_toolbar.urls)),
    ]
