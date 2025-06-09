import json
import logging

from ayuh_admission import (
    forms,
    models,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    UpdateView,
)

logger = logging.getLogger(__name__)


class AdmissionUpdateView(UpdateView):
    model = models.Admission
    form_class = forms.AdmissionForm
    template_name = "ayuh_admission/put_admission_template.html"

    def get_success_url(self):
        return reverse_lazy("get_admission", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["treatment_formset"] = forms.TreatmentFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["treatment_formset"] = forms.TreatmentFormSet(instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        treatment_formset = context["treatment_formset"]

        is_form_valid = form.is_valid()
        if not is_form_valid:
            logger.info(f"form is invalid. errors: {json.dumps(form.errors, indent=2)}")
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    attachment_formset=treatment_formset,
                )
            )

        self.object = form.save()

        treatments = treatment_formset.save(commit=False)
        for treatment in treatments:
            treatment.admission = self.object
            treatment.save()
        for obj in treatment_formset.deleted_objects:
            obj.delete()

        return super().form_valid(form)
