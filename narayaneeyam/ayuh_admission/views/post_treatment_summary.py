from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy

from ayuh_admission import (
    forms,
)

from django.views.generic.edit import FormView


from ayuh_admission.models import Admission


class TreatmentSummaryView(FormView):
    form_class = forms.TreatmentSummaryForm
    template_name = "ayuh_admission/post_treatment_summary_template.html"
    success_url = reverse_lazy("generate_discharge_invoice")

    def dispatch(self, request, *args, **kwargs):
        self.admission = get_object_or_404(Admission, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_formset(self, data=None):
        treatments = self.admission.treatment_admission.all()
        TreatmentCostFormSet = formset_factory(forms.TreatmentSummaryForm, extra=0)

        if data:
            return TreatmentCostFormSet(data)
        else:
            initial_data = [
                {
                    "treatment_id": treatment.id,
                    "treatment": treatment.treatment,
                    "therapist": treatment.therapist,
                    "treatment_date": treatment.treatment_date,
                }
                for treatment in treatments
            ]
            return TreatmentCostFormSet(initial=initial_data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admission"] = self.admission
        context["formset"] = self.get_formset(
            self.request.POST if self.request.method == "POST" else None
        )
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(request.POST)
        if formset.is_valid():
            self.request.session["discharge_data"] = formset.cleaned_data
            self.request.session["admission_id"] = self.admission.id
            return self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def form_valid(self, formset):
        return super().form_valid(formset)

    def form_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))
