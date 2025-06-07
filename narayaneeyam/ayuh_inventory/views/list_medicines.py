import logging

from ayuh_inventory.forms import (
    MedicinesForm,
)
from ayuh_inventory.models import (
    Medicine,
)
from django.views.generic import (
    ListView,
)

logger = logging.getLogger(__name__)


class MedicineListView(ListView):
    model = Medicine
    template_name = "ayuh_inventory/list_medicine_template.html"
    context_object_name = "medicines"

    def get_queryset(self):
        return Medicine.objects.prefetch_related("stock")
