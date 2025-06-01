from .list_medicines import MedicineListView
from .post_sale_of_medicines import MedicineSaleCreateView
from .post_sale_of_medicines_for_given_consultation import PrescriptionsSaleView

__all__ = [
    "MedicineListView",
    "MedicineSaleCreateView",
    "PrescriptionsSaleView",
]
