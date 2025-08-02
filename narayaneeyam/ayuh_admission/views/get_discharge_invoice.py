import tempfile

from django.http import (
    HttpResponse,
)
from django.views.generic import (
    View,
)
from weasyprint import (
    HTML,
)
from django.templatetags.static import static

from hashids import Hashids
from django.shortcuts import get_object_or_404
from django.template.loader import (
    get_template,
)
from django.conf import settings


class DischargeInvoiceView(View):

    def get_template_names(self):
        return ["ayuh_admission/get_discharge_invoice_template.html"]

    def get(self, request, *args, **kwargs):
        admission_id = kwargs.get("pk")

        logo_url = request.build_absolute_uri(
            static(settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_LOGO_IMAGE"))
        )

        invoice_number = Hashids(salt=settings.SECRET_KEY, min_length=6).encode(
            admission_id
        )

        context = {
            "logo_url": logo_url,
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
            "patient": {
                "name": "Suraj Vasudevan Bhattathiri",
                "gender": "MALE",
                "dob": "10-AUG-1987",
                "age": 38,
            },
            "patient_profile": {
                "pre_existing_health_conditions": "Spondylitis",
                "pre_existing_medications": "Thyroid",
                "known_allergies": "Dust, Mushrooms",
                "known_medication_allergies": "",
                "previous_surgeries": "",
                "patient_address": "HKRA-4, Near Sri Krishna Temple",
            },
            "consultation": {
                "consulting_doctor": "Dr. GOPIKA N",
                "consultation_date": "10-06-2025",
                "patient_concerns": "Shoulder pain spreading into arms",
                "patient_concerns_onset_from": "30-05-2025",
                "ongoing_medications_notes": "",
                "diagnosis": "Muscle tone",
            },
            "admission": {
                "admission_date": "07-06-2025",
                "treatment_overview": "Vasthi for 1 day, Dhara for 7 days",
                "room": "E4-ERN",
            },
            "treatment": [
                {
                    "treatment": "Vasthi",
                    "treatment_date": "07-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "07-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "08-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "09-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "10-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "11-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "12-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
                {
                    "treatment": "Dhaara",
                    "treatment_date": "13-06-2025",
                    "therapist": "Mrs SHALINI",
                    "amount": "100",
                },
            ],
            "discharge": {
                "discharge_date": "14-06-2025",
                "status": "CURED",
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
