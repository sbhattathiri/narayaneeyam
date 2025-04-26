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
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(f"{settings.FACILITY_NAME}/admin/", admin.site.urls),
    # path(f"{settings.FACILITY_NAME}/accounts/", include("django.contrib.auth.urls")),
    path(
        f"{settings.FACILITY_NAME}/login/",
        auth_views.LoginView.as_view(template_name="ayuh_home/login.html"),
        name="login",
    ),
    path(
        f"{settings.FACILITY_NAME}/logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_core.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_consultation.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_home.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_inventory.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_patient.urls")),
    path(f"{settings.FACILITY_NAME}/", include("ayuh_staff.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENABLE_DEBUG_TOOLBAR:
    from debug_toolbar.toolbar import (
        debug_toolbar_urls,
    )

    urlpatterns = urlpatterns + debug_toolbar_urls()
