from ayuh_admission import (
    models,
)
from django.views.generic.detail import (
    DetailView,
)


class AdmissionDetailView(DetailView):
    model = models.Admission
    template_name = "ayuh_admission/get_admission_template.html"
    context_object_name = "admission"
