from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)

from ayuh_staff import (
    forms,
    models,
)


class StaffCreateView(CreateView):
    model = models.Staff
    form_class = forms.StaffForm
    template_name = "ayuh_staff/post_staff_template.html"
    success_url = reverse_lazy("list_staff")
