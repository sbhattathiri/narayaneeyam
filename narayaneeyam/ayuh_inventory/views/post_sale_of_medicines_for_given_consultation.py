import json
import logging

from ayuh_inventory.models import (
    MedicineSale,
    MedicineSaleItem,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.db import (
    transaction,
)
from django.forms import (
    formset_factory,
)
from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    FormView,
)

from ayuh_consultation import (
    forms,
    models,
)

logger = logging.getLogger(__name__)


class PrescriptionsSaleView(LoginRequiredMixin, FormView):
    template_name = (
        "ayuh_inventory/post_sale_of_medicines_for_given_consultation_template.html"
    )
    form_class = forms.PrescriptionForGivenConsultationForm

    def get_success_url(self):
        # return reverse_lazy("get_medicine_sale", kwargs={"pk": self.sale.id})
        return reverse_lazy("post_payment_info", kwargs={"pk": self.sale.id})

    def get_formset(self):
        prescriptions = self.get_prescriptions()

        initial_data = [
            {
                "medicine": p.medicine,
                "quantity": p.quantity,
                "instructions": p.instructions,
            }
            for p in prescriptions
        ]

        logger.info(f"initial data: {initial_data}")

        FormSet = formset_factory(forms.PrescriptionForGivenConsultationForm, extra=0)

        if self.request.method == "POST":
            return FormSet(self.request.POST)

        return FormSet(initial=initial_data)

    def get_consultation(self):
        return get_object_or_404(
            models.Consultation, appointment_hash_id=self.kwargs["consultation_id"]
        )

    def get_prescriptions(self):
        consultation = self.get_consultation()
        return models.Prescription.objects.filter(consultation=consultation)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["consultation"] = self.get_consultation()
        context["formset"] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        context = self.get_context_data()
        formset = context["formset"]

        patient = self.get_consultation().patient

        if formset.is_valid():
            success = True
            formset.instance = self.get_formset()

            with transaction.atomic():
                self.sale = MedicineSale.objects.create(patient=patient)
                for item_form in formset:
                    medicine = item_form.cleaned_data["sku"]
                    quantity = item_form.cleaned_data["quantity"]

                    if medicine.stock.quantity < quantity:
                        form.add_error(
                            None, f"We don't have enough stock for {medicine.name}"
                        )
                        success = False
                        break

                    logger.info("deducting stock")
                    stock = medicine.stock
                    stock.quantity -= quantity
                    stock.save()

                    sale_item = MedicineSaleItem.objects.create(
                        sale=self.sale,
                        medicine=medicine,
                        quantity=quantity,
                    )

            if not success:
                return self.form_invalid(form)
        else:
            logger.info(
                f"formset is invalid. formset errors: {json.dumps(formset.errors, indent=2)}"
            )
            logger.info(
                f"formset is invalid. non form errors: {json.dumps(formset.non_form_errors(), indent=2)}"
            )
            return self.form_invalid(form)

        return redirect(self.get_success_url())
