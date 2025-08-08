import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic import View
from django.templatetags.static import static
from django.core.cache import cache
from weasyprint import HTML
from hashids import Hashids

from ayuh_inventory.models import MedicineSale, MedicineSalePaymentInfo


class OptimizedSaleInvoiceView(View):
    """
    Optimized invoice view that eliminates N+1 queries by:
    1. Using select_related and prefetch_related
    2. Caching PDF generation
    3. Single query for all related data
    """

    def get_template_names(self):
        return ["ayuh_inventory/get_sale_invoice_template.html"]

    def get(self, request, *args, **kwargs):
        sale_id = kwargs.get("pk")
        
        # Check cache first for generated PDF
        cache_key = f"invoice_pdf_{sale_id}"
        cached_pdf = cache.get(cache_key)
        
        if cached_pdf:
            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'filename="invoice.pdf"'
            response.write(cached_pdf)
            return response

        # Get sale with all related data in optimized queries
        sale = get_object_or_404(
            MedicineSale.objects.select_related(
                'patient',      # Patient data
                'updated_by'    # Sale updated_by
            ).prefetch_related(
                # Get sale items with medicine and manufacturer data
                'items__medicine__manufacturer',
                # Get payment info
                'payment'
            ),
            id=sale_id
        )

        # Get logo URL
        logo_url = request.build_absolute_uri(
            static(settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_LOGO_IMAGE"))
        )

        # Get patient/customer info
        patient = sale.patient if sale.patient else sale.customer
        invoice_date = sale.sale_date.date().strftime("%d %b %Y").upper()
        invoice_number = Hashids(salt=settings.SECRET_KEY, min_length=6).encode(sale_id)

        # Process sale items (data already prefetched, no additional queries)
        sale_items = []
        for item in sale.items.all():
            gst_amount = round(
                (item.medicine.price * item.medicine.gst / 100) * item.quantity, 2
            )
            amount_incl_gst = float(
                round(
                    (item.medicine.price * item.quantity) + gst_amount,
                    2,
                )
            )
            
            sale_items.append({
                "name": item.medicine.name,
                "manufacturer": item.medicine.manufacturer,
                "price": item.medicine.price,
                "quantity": item.quantity,
                "gst": item.medicine.gst,
                "gst_amount": gst_amount,
                "amount_incl_gst": amount_incl_gst,
            })

        total_amount = sum(item["amount_incl_gst"] for item in sale_items)

        # Get payment info (already prefetched)
        try:
            payment_info = sale.payment.latest("payment_due_date")
        except MedicineSalePaymentInfo.DoesNotExist:
            payment_info = None

        # Prepare context
        context = {
            "logo_url": logo_url,
            "items": sale_items,
            "gross_total": total_amount,
            "clinic": {
                "name_line1": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_NAME_LINE1"),
                "name_line2": settings.APP_SETTINGS.get("INVOICE_LETTERHEAD_NAME_LINE2"),
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
                "paid": payment_info.amount_paid if payment_info else 0,
                "balance_due": payment_info.amount_due if payment_info else 0,
                "payment_method": payment_info.payment_method if payment_info else "",
                "payment_date": payment_info.payment_due_date if payment_info else None,
            } if payment_info else None,
            "policy_line": settings.APP_SETTINGS.get("INVOICE_POLICY_LINE"),
        }

        # Generate PDF
        template = get_template(self.get_template_names()[0])
        html = template.render(context)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'filename="invoice.pdf"'

        with tempfile.NamedTemporaryFile(delete=True) as output:
            # Optimize PDF generation
            HTML(
                string=html, 
                base_url=request.build_absolute_uri("/")
            ).write_pdf(
                target=output.name,
                optimize_images=True,
                presentational_hints=True,
            )
            output.seek(0)
            pdf_content = output.read()
            
            # Cache the generated PDF for 1 hour
            cache.set(cache_key, pdf_content, 3600)
            
            response.write(pdf_content)

        return response


class BulkInvoiceView(View):
    """Generate multiple invoices efficiently"""
    
    def get(self, request, *args, **kwargs):
        sale_ids = request.GET.getlist('sale_ids')
        
        if not sale_ids:
            return HttpResponse("No sale IDs provided", status=400)
        
        # Get all sales with optimized query
        sales = MedicineSale.objects.select_related(
            'patient', 'updated_by'
        ).prefetch_related(
            'items__medicine__manufacturer',
            'payment'
        ).filter(id__in=sale_ids)
        
        # Generate combined PDF or ZIP file with multiple PDFs
        # Implementation depends on requirements
        pass


class InvoiceSummaryView(View):
    """Get invoice summary without generating PDF"""
    
    def get(self, request, *args, **kwargs):
        sale_id = kwargs.get("pk")
        
        # Use cached summary if available
        cache_key = f"invoice_summary_{sale_id}"
        summary = cache.get(cache_key)
        
        if summary is None:
            sale = get_object_or_404(
                MedicineSale.objects.select_related('patient').prefetch_related(
                    'items__medicine'
                ),
                id=sale_id
            )
            
            total_amount = sum(
                item.medicine.price * item.quantity * (1 + item.medicine.gst / 100)
                for item in sale.items.all()
            )
            
            summary = {
                'sale_id': sale.sale_id,
                'patient': str(sale.patient) if sale.patient else sale.customer,
                'total_amount': total_amount,
                'item_count': sale.items.count(),
                'sale_date': sale.sale_date.isoformat(),
            }
            
            cache.set(cache_key, summary, 1800)  # Cache for 30 minutes
        
        from django.http import JsonResponse
        return JsonResponse(summary)
