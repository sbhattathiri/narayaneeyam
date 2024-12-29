from ayuh_consultation import (
    forms,
    models,
)

from django.views.generic.detail import (
    DetailView,
)


class ConsultationDetailView(DetailView):
    model = models.Consultation
    template_name = "ayuh_consultation/get_consultation_template.html"
    context_object_name = "consultation"
