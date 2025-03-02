from django.urls import (
    path,
)

from ayuh_staff import (
    views,
)

urlpatterns = [
    path(
        "/ayuh/staff/list/",
        views.StaffListView.as_view(),
        name="list_staff",
    ),
    path(
        "/ayuh/staff/create/",
        views.StaffCreateView.as_view(),
        name="post_staff",
    ),
    path(
        "/ayuh/staff/<slug>/update/",
        views.StaffUpdateView.as_view(),
        name="put_staff",
    ),
]
