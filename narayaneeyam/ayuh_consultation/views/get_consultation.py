from django.views.generic.detail import (
    DetailView,
)

from ayuh_consultation import (
    models,
)


class ConsultationDetailView(DetailView):
    model = models.Consultation
    template_name = "ayuh_consultation/get_consultation_template.html"
    context_object_name = "consultation"
