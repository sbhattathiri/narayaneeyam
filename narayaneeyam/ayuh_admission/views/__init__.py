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

__all__ = [
    "AdmissionDetailView",
    "AdmissionListView",
    "AdmissionCreateView",
    "AdmissionUpdateView",
]
