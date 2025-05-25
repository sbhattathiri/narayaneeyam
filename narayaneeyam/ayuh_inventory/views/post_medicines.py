import logging

from django.urls import (
    reverse_lazy,
)
from django.db import transaction
from django.views.generic.edit import (
    CreateView,
)
from django.shortcuts import redirect

from ayuh_inventory import (
    forms,
    models,
)

logger = logging.getLogger(__name__)


class MedicineSaleCreateView(CreateView):

    model = models.MedicineSale
    form_class = forms.MedicineSaleForm
    template_name = "ayuh_inventory/post_medicine_sale_template.html"
    success_url = reverse_lazy("list_medicine")

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
                for item_form in formset:
                    if item_form.cleaned_data.get("DELETE"):
                        continue
                    medicine = item_form.cleaned_data["medicine"]
                    quantity = item_form.cleaned_data["quantity"]

                    if medicine.stock.quantity < quantity:
                        form.add_error(None, f"Not enough stock for {medicine.name}")
                        transaction.set_rollback(True)
                        return self.form_invalid(form)

                    logger.info("deducting stock")
                    stock = medicine.stock
                    stock.quantity -= quantity
                    stock.save()
                    medicine.save()

                formset.save()
            else:
                return self.form_invalid(form)

        return redirect(self.success_url)
