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


class InvoiceView(View):

    def get_template_names(self):
        return ["ayuh_inventory/narayaneeyam_invoice_template.html"]

    # def get_context_data(self, **kwargs):
    #     return {
    #         "invoice_number": "BNBY20240508",
    #         "invoice_date": "2024-05-08",
    #         "due_date": "2024-05-08",
    #         "recipient_name": "Baby, Bibin",
    #         "abn": "27 660 465 878",
    #         "company": {
    #             "name": "Ayurarogya Pty Ltd",
    #             "tagline": "healing space for better living",
    #             "address": "18 Detroit Avenue, Cranbourne East, Victoria 3977",
    #             "phone": "+61 470 432 355",
    #             "email": "info@ayurarogya.com.au",
    #         },
    #         "items": [
    #             {
    #                 "description": "Consultation Fee(Short)",
    #                 "gst_rate": 0,
    #                 "qty": 1,
    #                 "amount": 40.0,
    #             },
    #             {"description": "Treatment", "gst_rate": 10, "qty": 1, "amount": 40.0},
    #             {
    #                 "description": "Medicine Ext oil",
    #                 "gst_rate": 10,
    #                 "qty": 1,
    #                 "amount": 13.5,
    #             },
    #         ],
    #         "totals": {
    #             "subtotal": 93.5,
    #             "gst": 5.35,
    #             "total": 98.85,
    #             "paid": 0.0,
    #             "balance": 98.85,
    #         },
    #         "payment_method": "CARD",
    #         "bank_details": {
    #             "name": "Ayurarogya",
    #             "bsb": "083004",
    #             "account_number": "787255444",
    #         },
    #     }

    def get(self, request, *args, **kwargs):
        sale_id = kwargs.get("pk")

        logo_url = request.build_absolute_uri(
            static(settings.APP_SETTINGS.get("LETTERHEAD_LOGO_IMAGE"))
        )
        sign_url = request.build_absolute_uri(
            static(settings.APP_SETTINGS.get("LETTERHEAD_SIGN_IMAGE"))
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

        total_amount = sum(
            item["amount_incl_gst"]
            for item in sale_items
            if isinstance(item["amount_incl_gst"], (int, float))
        )

        total_amount2 = sum(item["amount_incl_gst"] for item in sale_items)

        payment_info = MedicineSalePaymentInfo.objects.filter(sale=sale).latest(
            "payment_due_date"
        )

        context = {
            "logo_url": logo_url,
            "sign_url": sign_url,
            "items": sale_items,
            "gross_total": total_amount,
            "gross_total2": total_amount2,
            "clinic": {
                "name": settings.APP_SETTINGS.get("FACILITY_NAME"),
                "tagline": settings.APP_SETTINGS.get("MOTTO"),
                "address1": settings.APP_SETTINGS.get("LETTERHEAD_ADDR_LINE1"),
                "address2": settings.APP_SETTINGS.get("LETTERHEAD_ADDR_LINE2"),
                "phone": settings.APP_SETTINGS.get("LETTERHEAD_CONTACT_PHONE"),
                "email": settings.APP_SETTINGS.get("LETTERHEAD_CONTACT_EMAIL"),
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
