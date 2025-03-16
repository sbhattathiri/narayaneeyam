import logging

from django.views.generic import (
    ListView,
)

from ayuh_inventory.models import (
    Medicine,
)

logger = logging.getLogger(__name__)


class MedicineListView(ListView):
    model = Medicine
    template_name = "ayuh_inventory/list_medicine_template.html"
    context_object_name = "medicines"
