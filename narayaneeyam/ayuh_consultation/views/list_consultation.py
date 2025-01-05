from django.views.generic import (
    ListView,
)

from ayuh_consultation import (
    models,
)


class ConsultationListView(ListView):
    model = models.Consultation
    template_name = "ayuh_consultation/list_consultation_template.html"
    context_object_name = "consultations"
