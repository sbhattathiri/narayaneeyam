from django.conf import (
    settings,
)


def ayuh_context(request):
    return {
        "FACILITY_NAME": settings.APP_SETTINGS["FACILITY_NAME"],
        "MOTTO": settings.APP_SETTINGS["MOTTO"],
        "PRIMARY_COLOR": settings.APP_SETTINGS["PRIMARY_COLOR"],
    }
