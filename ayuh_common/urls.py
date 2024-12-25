from django.urls import path

from ayuh_common import views

urlpatterns = [
    path("", views.home, name="home"),
]
