import logging

from django.views.generic.edit import FormView
from django.forms import formset_factory
from django.urls import (
    reverse_lazy,
)
from django.shortcuts import get_object_or_404, redirect
from ayuh_consultation import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)


class PrescriptionsSaleView(LoginRequiredMixin, FormView):
    template_name = (
        "ayuh_inventory/post_medicine_sale_for_given_consultation_template.html"
    )
    form_class = forms.PrescriptionForGivenConsultationForm

    def get_success_url(self):
        return reverse_lazy("list_consultation")

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
        formset = self.get_formset()
        if formset.is_valid():
            for form in formset:
                # process SKU and quantity
                print(form.cleaned_data)
            return redirect(self.success_url)
        context = self.get_context_data(formset=formset)
        return self.render_to_response(context)
