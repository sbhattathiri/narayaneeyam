from django.shortcuts import (
    render,
)


def billing_info(request):
    return render(request, "billing_info.html", {})
