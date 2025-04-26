from django.views.generic import FormView

from django.shortcuts import redirect

from ayuh_consultation import (
    forms,
    models,
)


class ConsultationSearchView(FormView):
    template_name = "ayuh_consultation/post_search_consultation.html"
    form_class = forms.ConsultationSearchForm

    def form_valid(self, form):
        consultation_id = form.cleaned_data["consultation_id"]
        if not models.Consultation.objects.filter(
            appointment_hash_id=consultation_id
        ).exists():
            form.add_error("consultation_id", "Consultation not found.")
            return self.form_invalid(form)

        return redirect(
            "post_sale_of_prescriptions_for_given_consultation",
            consultation_id=consultation_id,
        )
