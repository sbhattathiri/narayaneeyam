from django.shortcuts import (
    render,
)


def home(request):
    return render(request, "ayuh_home/home_landing_template.html", context={})


def patient_management(request):
    return render(
        request,
        "ayuh_home/patient_consultation_management_landing_template.html",
        context={},
    )
