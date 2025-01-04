from .list_patient import (
    PatientListView,
)
from .post_patient import (
    PatientCreateView,
)
from .put_patient import (
    PatientUpdateView,
)

__all__ = [
    "PatientListView",
    "PatientCreateView",
    "PatientUpdateView",
]
