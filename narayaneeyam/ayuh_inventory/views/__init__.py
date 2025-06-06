from .list_medicines import (
    MedicineListView,
)
from .post_sale_of_medicines import (
    MedicineSaleCreateView,
)
from .post_sale_of_medicines_for_given_consultation import (
    PrescriptionsSaleView,
)
from .post_search_consultation import (
    ConsultationSearchView,
)

__all__ = [
    "ConsultationSearchView",
    "MedicineListView",
    "MedicineSaleCreateView",
    "PrescriptionsSaleView",
]
