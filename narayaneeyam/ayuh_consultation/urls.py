from ayuh_consultation import (
    views,
)

from django.urls import (
    path,
)

urlpatterns = [
    path(
        "list",
        views.ConsultationListView.as_view(),
        name="list_consultation",
    ),
    path(
        "new/",
        views.AppointmentCreateView.as_view(),
        name="post_appointment",
    ),
    path(
        "create/",
        views.ConsultationCreateView.as_view(),
        name="post_consultation",
    ),
    path(
        "<uuid:pk>/",
        views.ConsultationDetailView.as_view(),
        name="get_consultation",
    ),
    path(
        "<uuid:pk>/update/",
        views.ConsultationUpdateView.as_view(),
        name="put_consultation",
    ),
]
