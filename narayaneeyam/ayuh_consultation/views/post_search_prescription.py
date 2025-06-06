from django.shortcuts import (
    redirect,
)
from django.views.generic import (
    FormView,
)

from ayuh_consultation import (
    forms,
    models,
)
from ayuh_patient.models import (
    Patient,
)


class PrescriptionSearchView(FormView):
    template_name = "ayuh_consultation/post_search_prescription.html"
    form_class = forms.PrescriptionSearchForm

    def form_valid(self, form):
        patient_registration_id = form.cleaned_data["patient_registration_id"]
        if not Patient.objects.filter(
            patient_registration_id=patient_registration_id
        ).exists():
            form.add_error("patient_registration_id", "Patient not found.")
            return self.form_invalid(form)

        return redirect(
            "prescription_history",
            patient_registration_id=patient_registration_id,
        )
