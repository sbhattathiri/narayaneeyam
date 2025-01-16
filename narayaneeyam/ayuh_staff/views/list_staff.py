import logging

from django.views.generic import (
    ListView,
)


from ayuh_staff import (
    models,
)

logger = logging.getLogger(__name__)


class StaffListView(ListView):
    model = models.Staff
    template_name = "ayuh_staff/list_staff_template.html"
    context_object_name = "staffs"
    slug_field = "staff_hash_id"
