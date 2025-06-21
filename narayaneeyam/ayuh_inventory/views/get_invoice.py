import tempfile

from ayuh import (
    settings,
)
from django.http import (
    HttpResponse,
)
from django.template.loader import (
    get_template,
)
from django.views.generic import (
    View,
)
from weasyprint import (
    HTML,
)


class InvoiceView(View):

    def get_template_names(self):
        if settings.ACTIVE_APP_PROFILE == "AYURAROGYA":
            return ["ayuh_inventory/ayurarogya_invoice_template.html"]
        return ["ayuh_inventory/narayaneeyam_invoice_template.html"]

    def get_context_data(self, **kwargs):
        # invoice = get_object_or_404(Invoice, pk=kwargs["pk"]

        return {
            "invoice_number": "BNBY20240508",
            "invoice_date": "2024-05-08",
            "due_date": "2024-05-08",
            "recipient_name": "Baby, Bibin",
            "abn": "27 660 465 878",
            "company": {
                "name": "Ayurarogya Pty Ltd",
                "tagline": "healing space for better living",
                "address": "18 Detroit Avenue, Cranbourne East, Victoria 3977",
                "phone": "+61 470 432 355",
                "email": "info@ayurarogya.com.au",
            },
            "items": [
                {
                    "description": "Consultation Fee(Short)",
                    "gst_rate": 0,
                    "qty": 1,
                    "amount": 40.0,
                },
                {"description": "Treatment", "gst_rate": 10, "qty": 1, "amount": 40.0},
                {
                    "description": "Medicine Ext oil",
                    "gst_rate": 10,
                    "qty": 1,
                    "amount": 13.5,
                },
            ],
            "totals": {
                "subtotal": 93.5,
                "gst": 5.35,
                "total": 98.85,
                "paid": 0.0,
                "balance": 98.85,
            },
            "payment_method": "CARD",
            "bank_details": {
                "name": "Ayurarogya",
                "bsb": "083004",
                "account_number": "787255444",
            },
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        template = get_template(self.get_template_names()[0])
        html = template.render(context)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'filename="invoice.pdf"'

        with tempfile.NamedTemporaryFile(delete=True) as output:
            HTML(string=html).write_pdf(target=output.name)
            output.seek(0)
            response.write(output.read())

        return response
