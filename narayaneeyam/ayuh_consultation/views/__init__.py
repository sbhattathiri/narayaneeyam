from .get_consultation import (
    ConsultationDetailView,
)
from .list_consultation import (
    ConsultationListView,
)
from .post_consultation import (
    ConsultationCreateView,
)
from .put_consultation import (
    ConsultationUpdateView,
)

__all__ = [
    "ConsultationCreateView",
    "ConsultationDetailView",
    "ConsultationUpdateView",
    "ConsultationListView",
]
