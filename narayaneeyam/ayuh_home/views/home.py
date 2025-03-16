from django.shortcuts import render, redirect


def narayaneeyam_home(request):
    return render(request, "ayuh_home/home_template.html", context={})


def narayaneeyam_admin(request):
    return render(request, "ayuh_home/admin_home_template.html", context={})


def narayaneeyam_admission(request):
    return render(
        request,
        "ayuh_home/admissions_home_template.html",
        context={},
    )
