from ayuh_inventory import (
    models,
)
from django.views.generic.detail import (
    DetailView,
)


class MedicineSaleDetailView(DetailView):
    model = models.MedicineSale
    template_name = "ayuh_inventory/get_medicine_sale_template.html"
    pk_url_kwarg = "pk"
    context_object_name = "sale"
