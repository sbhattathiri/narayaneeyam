from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)

from ayuh_inventory import (
    forms,
    models,
)


class MedicineSaleCreateView(CreateView):
    model = models.MedicineSale
    form_class = forms.MedicineSalesForm
    template_name = "ayuh_inventory/post_medicine_sale_template.html"
    success_url = reverse_lazy("list_medicine")
