from ayuh_consultation import (
    views,
)

from django.urls import (
    path,
)


urlpatterns = [
    path("", views.ListConsultation.as_view(), name="list_consultation"),
    path("add/", views.AddConsultation.as_view(), name="add_consultation"),
    path(
        "<uuid:pk>/edit/",
        views.UpdateConsultation.as_view(),
        name="update_consultation",
    ),
]
