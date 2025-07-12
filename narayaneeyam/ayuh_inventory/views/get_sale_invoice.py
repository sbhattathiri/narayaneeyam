import tempfile

from ayuh import (
    settings,
)
from django.http import (
    HttpResponse,
)
from django.shortcuts import get_object_or_404
from django.template.loader import (
    get_template,
)
from django.views.generic import (
    View,
)
from weasyprint import (
    HTML,
)
from django.templatetags.static import static

from ayuh_inventory.models import MedicineSale, MedicineSalePaymentInfo
from hashids import Hashids


class SaleInvoiceView(View):

    def get_template_names(self):
        return ["ayuh_inventory/get_sale_invoice_template.html"]

    def get(self, request, *args, **kwargs):
        sale_id = kwargs.get("pk")

        logo_url = request.build_absolute_uri(
            static(settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_LOGO_IMAGE"))
        )

        sale = get_object_or_404(MedicineSale, id=sale_id)

        patient = sale.patient if sale.patient else sale.customer
        invoice_date = sale.sale_date.date().strftime("%d %b %Y").upper()
        invoice_number = Hashids(salt=settings.SECRET_KEY, min_length=6).encode(sale_id)

        items = sale.items.select_related("medicine").all()

        sale_items = [
            {
                "name": item.medicine.name,
                "manufacturer": item.medicine.manufacturer,
                "price": item.medicine.price,
                "quantity": item.quantity,
                "gst": item.medicine.gst,
                "gst_amount": round(
                    (item.medicine.price * item.medicine.gst / 100) * item.quantity, 2
                ),
                "amount_incl_gst": float(
                    round(
                        (item.medicine.price * item.quantity)
                        + (item.medicine.price * item.medicine.gst / 100)
                        * item.quantity,
                        2,
                    )
                ),
            }
            for item in items
        ]

        total_amount = sum(item["amount_incl_gst"] for item in sale_items)

        payment_info = MedicineSalePaymentInfo.objects.filter(sale=sale).latest(
            "payment_due_date"
        )

        context = {
            "logo_url": logo_url,
            "items": sale_items,
            "gross_total": total_amount,
            "clinic": {
                "name_line1": settings.APP_SETTINGS.get(
                    "INVOICE_LETTERHEAD_NAME_LINE1"
                ),
                "name_line2": settings.APP_SETTINGS.get(
                    "INVOICE_LETTERHEAD_NAME_LINE2"
                ),
                "tagline": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_MOTTO"),
                "address1": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_ADDR_LINE1"),
                "address2": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_ADDR_LINE2"),
                "phone": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_CONTACT_PHONE"),
                "email": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_CONTACT_EMAIL"),
                "website": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_WEBSITE"),
            },
            "invoice_number": invoice_number,
            "patient": patient,
            "invoice_date": invoice_date,
            "payment": {
                "paid": payment_info.amount_paid,
                "balance_due": payment_info.amount_due,
                "payment_method": payment_info.payment_method,
                "payment_date": payment_info.payment_due_date,
            },
            "policy_line": settings.APP_SETTINGS.get("INVOICE_POLICY_LINE"),
        }

        template = get_template(self.get_template_names()[0])
        html = template.render(context)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'filename="invoice.pdf"'

        with tempfile.NamedTemporaryFile(delete=True) as output:
            HTML(string=html, base_url=request.build_absolute_uri("/")).write_pdf(
                target=output.name
            )
            output.seek(0)
            response.write(output.read())

        return response
