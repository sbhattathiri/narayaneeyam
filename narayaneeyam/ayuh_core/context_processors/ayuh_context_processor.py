from django.conf import (
    settings,
)


def ayuh_context(request):
    return {
        "FACILITY_NAME": settings.APP_SETTINGS.get("APPLICATION_FACILITY_NAME"),
        "MOTTO": settings.APP_SETTINGS.get("APPLICATION_MOTTO"),
        "PRIMARY_COLOR": settings.APP_SETTINGS.get("APPLICATION_PRIMARY_COLOR"),
        "BUTTON_TEXT_COLOR": settings.APP_SETTINGS.get("APPLICATION_BUTTON_TEXT_COLOR"),
    }
