from django.conf import (
    settings,
)
from django.conf.urls.static import (
    static,
)
from django.contrib import (
    admin,
)
from django.contrib.auth import views as auth_views
from django.urls import (
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

prefix = settings.APP_NAME

urlpatterns = [
    path(f"{prefix}/admin/", admin.site.urls),
    path(
        f"{prefix}/login/",
        auth_views.LoginView.as_view(template_name="ayuh_home/login.html"),
        name="login",
    ),
    path(
        f"{prefix}/logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path(f"{prefix}/", include("ayuh_core.urls")),
    path(f"{prefix}/", include("ayuh_consultation.urls")),
    path(f"{prefix}/", include("ayuh_admission.urls")),
    path(f"{prefix}/", include("ayuh_home.urls")),
    path(f"{prefix}/", include("ayuh_facility.urls")),
    path(f"{prefix}/", include("ayuh_inventory.urls")),
    path(f"{prefix}/", include("ayuh_patient.urls")),
    path(f"{prefix}/", include("ayuh_staff.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENABLE_DEBUG_TOOLBAR:
    from debug_toolbar.toolbar import (
        debug_toolbar_urls,
    )

    urlpatterns = urlpatterns + debug_toolbar_urls()
