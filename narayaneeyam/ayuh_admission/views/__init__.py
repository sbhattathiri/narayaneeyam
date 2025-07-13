from .get_admission import (
    AdmissionDetailView,
)
from .list_admission import (
    AdmissionListView,
)
from .post_admission import (
    AdmissionCreateView,
)
from .put_admission import (
    AdmissionUpdateView,
)

# from .post_treatment_summary import TreatmentSummaryView
from .get_discharge_invoice import DischargeInvoiceView

__all__ = [
    "AdmissionDetailView",
    "AdmissionListView",
    "AdmissionCreateView",
    "AdmissionUpdateView",
    "DischargeInvoiceView",
    # "TreatmentSummaryView",
]
