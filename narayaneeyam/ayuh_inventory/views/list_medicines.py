import logging

from django.views.generic import (
    ListView,
)

from ayuh_inventory.forms import MedicinesForm
from ayuh_inventory.models import (
    Medicine,
)

logger = logging.getLogger(__name__)


class MedicineListView(ListView):
    model = Medicine
    # form_class = MedicinesForm
    template_name = "ayuh_inventory/list_medicine_template.html"
    context_object_name = "medicines"

    def get_queryset(self):
        return Medicine.objects.prefetch_related("stock")
