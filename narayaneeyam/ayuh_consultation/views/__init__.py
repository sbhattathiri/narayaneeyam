from .get_consultation import (
    ConsultationDetailView,
)
from .list_consultation import (
    ConsultationListView,
)
from .list_prescription_history import (
    PrescriptionHistoryListView,
)
from .post_consultation import (
    ConsultationCreateView,
)
from .post_search_prescription import (
    PrescriptionSearchView,
)
from .put_consultation import (
    ConsultationUpdateView,
)

__all__ = [
    "ConsultationCreateView",
    "ConsultationDetailView",
    "ConsultationUpdateView",
    "ConsultationListView",
    "PrescriptionSearchView",
    "PrescriptionHistoryListView",
]
