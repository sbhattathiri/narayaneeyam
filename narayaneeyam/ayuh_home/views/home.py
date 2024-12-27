from datetime import (
    datetime,
)

import pytz

from django.shortcuts import (
    render,
)

ist_timezone = pytz.timezone("Asia/Kolkata")


def home(request):
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "home.html", context=context)


def billing_management(request):
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "billing_management.html", context=context)


def inventory_management(request):
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "inventory_management.html", context=context)


def patient_management(request):
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "patient_management.html", context=context)


def reminders(request):
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "reminders.html", context=context)
