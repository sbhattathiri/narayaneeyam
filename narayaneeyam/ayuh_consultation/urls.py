from django.urls import (
    path,
)

from ayuh_consultation import (
    views,
)

urlpatterns = [
    path(
        "create/",
        views.ConsultationCreateView.as_view(),
        name="post_consultation",
    ),
    path(
        "<int:pk>/",
        views.ConsultationDetailView.as_view(),
        name="get_consultation",
    ),
    path(
        "list",
        views.ConsultationListView.as_view(),
        name="list_consultation",
    ),
    path(
        "<int:pk>/update/",
        views.ConsultationUpdateView.as_view(),
        name="put_consultation",
    ),
]
