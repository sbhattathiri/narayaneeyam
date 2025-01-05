from django.shortcuts import (
    redirect,
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


class ConsultationUpdateView(UpdateView):
    model = models.Consultation
    form_class = forms.ConsultationForm
    template_name = "ayuh_consultation/put_consultation_template.html"
    success_url = reverse_lazy("list_consultation")

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
            attachment_formset.instance = self.object
            attachment_formset.save()
            prescription_formset.instance = self.object
            prescription_formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)
