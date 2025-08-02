from decimal import Decimal

from ayuh_inventory import (
    forms,
    models,
)
from django.views.generic.edit import (
    CreateView,
)
from django.urls import (
    reverse_lazy,
)
from django.db.models import F, Sum, ExpressionWrapper, DecimalField

from ayuh_inventory.models import MedicineSaleItem


class MedicineSalePaymentInfoCreateView(CreateView):
    model = models.MedicineSalePaymentInfo
    form_class = forms.MedicineSalePaymentInfoForm
    template_name = "ayuh_inventory/post_payment_info_template.html"
    pk_url_kwarg = "pk"
    context_object_name = "sale"

    def get_success_url(self):
        return reverse_lazy("get_medicine_sale", kwargs={"pk": self.object.sale.id})

    def get_initial(self):
        sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
        medicine_sale_items_query_set = (
            MedicineSaleItem.objects.filter(sale=sale)
            .select_related("medicine")
            .annotate(
                sale_amount=ExpressionWrapper(
                    F("quantity") * F("medicine__price"),
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
                gst_amount=ExpressionWrapper(
                    F("quantity") * F("medicine__price") * F("medicine__gst"),
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                ),
            )
        )
        totals = medicine_sale_items_query_set.aggregate(
            total_sale_amount=Sum("sale_amount"), total_gst_amount=Sum("gst_amount")
        )

        total_sale_amount = totals["total_sale_amount"] or Decimal(0.00)
        total_gst_amount = totals["total_gst_amount"] or Decimal(0.00)

        return {
            "sale": sale,
            "total_sale_amount": total_sale_amount,
            "total_gst_amount": total_gst_amount,
            "total_sale_amount_with_gst": total_sale_amount + total_gst_amount,
        }

    def form_valid(self, form):
        form.instance.sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
