import logging

from ayuh_inventory import (
    forms,
    models,
)
from ayuh_inventory.models import (
    MedicineSaleItem,
)
from django.db import (
    transaction,
)
from django.shortcuts import (
    redirect,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)

logger = logging.getLogger(__name__)


class MedicineSaleCreateView(CreateView):

    model = models.MedicineSale
    form_class = forms.MedicineSaleForm
    template_name = "ayuh_inventory/post_sale_of_medicines_template.html"

    def get_success_url(self):
        return reverse_lazy("post_payment_info", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = forms.MedicineSaleItemsFormSet(self.request.POST)
        else:
            context["formset"] = forms.MedicineSaleItemsFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]

        with transaction.atomic():
            self.object = form.save()

            if formset.is_valid():
                formset.instance = self.object
                logger.info(f"# of forms {len(formset)}")

                for item_form in formset:

                    if item_form.cleaned_data.get("DELETE"):
                        continue

                    medicine = item_form.cleaned_data["medicine"]
                    quantity = item_form.cleaned_data["quantity"]

                    logger.info(f"sale for medicine: {medicine} | quantity: {quantity}")

                    if medicine.stock.quantity < quantity:
                        form.add_error(
                            None, f"We don't have enough stock for {medicine.name}"
                        )
                        transaction.set_rollback(True)
                        return self.form_invalid(form)

                    logger.info("deducting stock")
                    stock = medicine.stock
                    stock.quantity -= quantity
                    stock.save()
                    medicine.save()

                    logger.info(
                        f"creating sale item for {self.object}:{self.object.id} | medicine: {medicine} | quantity: {quantity}"
                    )

                    # sale_item = MedicineSaleItem.objects.create(
                    #     sale=self.object,
                    #     medicine=medicine,
                    #     quantity=quantity,
                    # )

                formset.save()
            else:
                return self.form_invalid(form)

        return redirect(self.get_success_url())
