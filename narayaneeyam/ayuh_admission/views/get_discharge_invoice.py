from django.http import (
    HttpResponse,
)
from django.views.generic import (
    View,
)


class DischargeInvoiceView(View):

    def get_template_names(self):
        return ["ayuh_admission/get_discharge_invoice_template.html"]

    def get(self, request, *args, **kwargs):
        admission_id = kwargs.get("pk")

        return HttpResponse(
            f"PDF for admission ID {admission_id}", content_type="text/plain"
        )
