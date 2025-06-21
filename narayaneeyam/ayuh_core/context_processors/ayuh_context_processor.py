from django.conf import (
    settings,
)


def ayuh_context(request):
    return {
        "FACILITY_NAME": settings.APP_SETTINGS.get("FACILITY_NAME"),
        "MOTTO": settings.APP_SETTINGS.get("MOTTO"),
        "PRIMARY_COLOR": settings.APP_SETTINGS.get("PRIMARY_COLOR"),
        "BUTTON_TEXT_COLOR": settings.APP_SETTINGS.get("BUTTON_TEXT_COLOR"),
    }
