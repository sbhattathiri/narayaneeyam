from ayuh_consultation import (
    models,
)

from django.views.generic import (
    ListView,
)


class ConsultationListView(ListView):
    model = models.Consultation
    template_name = "ayuh_consultation/list_consultation_template.html"
    context_object_name = "consultations"
