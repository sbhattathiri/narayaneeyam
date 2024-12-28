from ayuh_patient import (
    forms,
    models,
)

from django.urls import (
    reverse_lazy,
)
from django.views.generic.detail import (
    DetailView,
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)


class PatientProfile(DetailView):
    model = models.PatientProfile
    template_name = "patient_management_view_patient.html"
    context_object_name = "patient"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = forms.PatientProfile(instance=self.object)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = True
            field.widget.attrs["disabled"] = True
        context["form"] = form
        return context


class AddPatientProfile(CreateView):
    model = models.PatientProfile
    form_class = forms.PatientProfile
    template_name = "patient_management_add_patient.html"

    def get_success_url(self):
        return reverse_lazy("view_patient", kwargs={"pk": self.object.pk})


class UpdatePatientProfile(UpdateView):
    model = models.PatientProfile
    form_class = forms.PatientProfile
    template_name = "patient_management_edit_patient.html"

    def get_success_url(self):
        return reverse_lazy("view_patient", kwargs={"pk": self.object.pk})
