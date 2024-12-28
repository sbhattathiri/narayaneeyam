from django.shortcuts import (
    render,
)


def billing_management(request):
    return render(request, "billing_management.html", context={})


def expense_management(request):
    return render(request, "expense_management.html", context={})


def home(request):
    return render(request, "home.html", context={})


def human_resource_management(request):
    return render(request, "human_resource_management.html", context={})


def inventory_management(request):
    return render(request, "inventory_management.html", context={})


def patient_management(request):
    return render(request, "patient_management.html", context={})


def publicity_management(request):
    return render(request, "publicity_management.html", context={})


def reminders(request):
    return render(request, "reminders.html", context={})
