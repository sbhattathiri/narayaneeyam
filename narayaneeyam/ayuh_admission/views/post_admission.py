from ayuh_admission import (
    forms,
    models,
)
from django.urls import (
    reverse_lazy,
)
from django.views.generic.edit import (
    CreateView,
)


class AdmissionCreateView(CreateView):
    model = models.Admission
    form_class = forms.AdmissionForm
    template_name = "ayuh_admission/post_admission_template.html"
    success_url = reverse_lazy("list_admission")
