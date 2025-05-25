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

from .post_search_consultation import ConsultationSearchView
from .list_prescription_history import PrescriptionHistoryListView
from .post_search_prescription import PrescriptionSearchView

__all__ = [
    "ConsultationCreateView",
    "ConsultationDetailView",
    "ConsultationUpdateView",
    "ConsultationListView",
    "ConsultationSearchView",
    "PrescriptionSearchView",
    "PrescriptionHistoryListView",
]
