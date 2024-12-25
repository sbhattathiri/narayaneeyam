from datetime import (
    datetime,
)

import pytz
from django.shortcuts import (
    render,
)


def home(request):
    ist_timezone = pytz.timezone("Asia/Kolkata")
    context = {
        "current_date": datetime.now(ist_timezone).strftime("%B %d, %Y"),
        "current_time": datetime.now(ist_timezone).strftime("%I:%M %p"),
    }
    return render(request, "home.html", context=context)
