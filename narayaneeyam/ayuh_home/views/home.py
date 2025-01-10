from django.shortcuts import (
    render,
)


def home(request):
    return render(request, "ayuh_home/home_template.html", context={})


def admin(request):
    return render(request, "ayuh_home/admin_home_template.html", context={})


def admission(request):
    return render(
        request,
        "ayuh_home/admissions_home_template.html",
        context={},
    )


def inventory(request):
    return render(
        request,
        "ayuh_home/inventory_home_template.html",
        context={},
    )
