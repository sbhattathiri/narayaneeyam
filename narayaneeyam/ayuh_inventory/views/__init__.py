from .list_medicines import MedicineListView
from .post_medicines import MedicineSaleCreateView
from .post_sale_of_prescriptions_for_given_consultation import PrescriptionsSaleView

__all__ = [
    "MedicineListView",
    "MedicineSaleCreateView",
    "PrescriptionsSaleView",
]
