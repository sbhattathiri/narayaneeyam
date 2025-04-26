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
from .post_sale_of_prescriptions_for_given_consultation import PrescriptionsSaleView
from .post_search_consultation import ConsultationSearchView

__all__ = [
    "ConsultationCreateView",
    "ConsultationDetailView",
    "ConsultationUpdateView",
    "ConsultationListView",
    "ConsultationSearchView",
    "PrescriptionsSaleView",
]
