import json
import logging

from django.conf import (
    settings,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    UpdateView,
)

from ayuh_consultation import (
    forms,
    models,
)

logger = logging.getLogger(__name__)


class ConsultationUpdateView(UpdateView):
    model = models.Consultation
    form_class = forms.ConsultationForm
    template_name = "ayuh_consultation/put_consultation_template.html"

    def get_success_url(self):
        return reverse_lazy("get_consultation", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["attachment_formset"] = forms.ConsultationAttachmentFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            context["prescription_formset"] = forms.PrescriptionFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["attachment_formset"] = forms.ConsultationAttachmentFormSet(
                instance=self.object
            )
            context["prescription_formset"] = forms.PrescriptionFormSet(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        attachment_formset = context["attachment_formset"]
        prescription_formset = context["prescription_formset"]

        is_form_valid = form.is_valid()
        if not is_form_valid:
            logger.info(f"form is invalid. errors: {json.dumps(form.errors, indent=2)}")
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    attachment_formset=attachment_formset,
                    prescription_formset=prescription_formset,
                )
            )

        is_attachment_valid = attachment_formset.is_valid()
        if not is_attachment_valid:
            logger.info(
                f"attachment_formset is invalid. formset errors: {json.dumps(attachment_formset.errors, indent=2)}"
            )
            logger.info(
                f"attachment_formset is invalid. non form errors: {json.dumps(attachment_formset.non_form_errors(), indent=2)}"
            )
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    attachment_formset=attachment_formset,
                    prescription_formset=prescription_formset,
                )
            )

        is_prescription_valid = prescription_formset.is_valid()
        if not is_prescription_valid:
            logger.info(
                f"prescription_formset is invalid. formset errors: {json.dumps(prescription_formset.errors, indent=2)}"
            )
            logger.info(
                f"prescription_formset is invalid. non form errors: {json.dumps(prescription_formset.non_form_errors(), indent=2)}"
            )
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    attachment_formset=attachment_formset,
                    prescription_formset=prescription_formset,
                )
            )

        is_consent_mandatory = settings.APP_SETTINGS.get(
            "PATIENT_CONSENT_MANDATORY", True
        )

        valid_attachment_forms = [
            attachment_form
            for attachment_form in attachment_formset.forms
            if attachment_form not in attachment_formset.deleted_forms
            and attachment_form.cleaned_data
            and not attachment_form.cleaned_data.get("DELETE", False)
        ]

        if is_consent_mandatory:
            if not valid_attachment_forms:
                form.add_error(None, "Please attach the patient consent form.")
                logger.info("consent not attached")
                return self.render_to_response(
                    self.get_context_data(
                        form=form,
                        attachment_formset=attachment_formset,
                        prescription_formset=prescription_formset,
                    )
                )

        self.object = form.save()

        attachments = attachment_formset.save(commit=False)
        for attachment in attachments:
            attachment.consultation = self.object
            attachment.save()
        for obj in attachment_formset.deleted_objects:
            obj.delete()

        prescriptions = prescription_formset.save(commit=False)
        for prescription in prescriptions:
            prescription.consultation = self.object
            prescription.save()
        for obj in prescription_formset.deleted_objects:
            obj.delete()

        return super().form_valid(form)
