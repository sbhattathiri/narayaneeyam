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
        if attachment_formset.is_valid() and prescription_formset.is_valid():
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

            # return redirect(self.get_success_url())
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
