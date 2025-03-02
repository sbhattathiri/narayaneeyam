import logging

from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    UpdateView,
)

from ayuh_staff import (
    forms,
    models,
)

logger = logging.getLogger(__name__)


class StaffUpdateView(UpdateView):
    model = models.Staff
    slug_field = "staff_hash_id"
    form_class = forms.StaffForm
    template_name = "ayuh_staff/put_staff_template.html"
    success_url = reverse_lazy("list_staff")
