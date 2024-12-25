from django.shortcuts import (
    render,
)


def inventory_info(request):
    return render(request, "inventory_info.html", {})
