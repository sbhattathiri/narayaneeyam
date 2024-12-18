from django.urls import path

from backend.ayuh_common import views

urlpatterns = [
    path("", views.home, name="home"),
]
