from .get_consultation import (
    ConsultationDetailView,
)
from .list_consultation import (
    ConsultationListView,
)
from .post_appointment import (
    AppointmentCreateView,
)
from .post_consultation import (
    ConsultationCreateView,
)
from .put_consultation import (
    ConsultationUpdateView,
)

__all__ = [
    "AppointmentCreateView",
    "ConsultationCreateView",
    "ConsultationDetailView",
    "ConsultationUpdateView",
    "ConsultationListView",
]
