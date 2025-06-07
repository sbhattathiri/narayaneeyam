from .put_admission import AdmissionUpdateView
from .list_admission import AdmissionListView
from .post_admission import AdmissionCreateView
from .get_admission import AdmissionDetailView

__all__ = [
    "AdmissionDetailView",
    "AdmissionListView",
    "AdmissionCreateView",
    "AdmissionUpdateView",
]
