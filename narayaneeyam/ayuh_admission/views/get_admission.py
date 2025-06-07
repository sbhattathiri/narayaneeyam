from django.views.generic.detail import (
    DetailView,
)

from ayuh_admission import (
    models,
)


class AdmissionDetailView(DetailView):
    model = models.Admission
    template_name = "ayuh_admission/get_admission_template.html"
    context_object_name = "admission"

    # def get_object(self):
    #     obj = super().get_object()
    #     # Do something with `obj`
    #     return obj
