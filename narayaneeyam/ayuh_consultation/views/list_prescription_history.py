import logging

from django.db.models import (
    F,
)
from django.shortcuts import (
    get_object_or_404,
)
from django.views.generic import (
    ListView,
)

from ayuh_consultation import (
    models,
)
from ayuh_patient.models import (
    Patient,
)

logger = logging.getLogger(__name__)


class PrescriptionHistoryListView(ListView):
    model = models.Prescription
    template_name = "ayuh_consultation/list_prescription_history_template.html"
    context_object_name = "prescription_history"
    paginate_by = 20  # Add pagination for better performance

    def get_queryset(self):
        """
        OPTIMIZED VERSION - Eliminates N+1 queries by:
        1. Using select_related for consultation, patient, and doctor
        2. Getting patient once and reusing
        3. Removing unnecessary logging in loop
        """
        # Get patient once with optimized query
        self.patient = get_object_or_404(
            Patient.objects.select_related('updated_by'),
            patient_registration_id=self.kwargs["patient_registration_id"]
        )

        # Get prescriptions with all related data in one query
        prescriptions = models.Prescription.objects.select_related(
            'consultation__patient',    # Patient data
            'consultation__doctor',     # Doctor data
            'consultation__updated_by', # Consultation updated_by
            'updated_by'               # Prescription updated_by
        ).filter(
            consultation__patient=self.patient
        ).order_by('-consultation__consultation_date')  # Most recent first

        return prescriptions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_registration_id"] = self.patient.patient_registration_id
        context["patient_full_name"] = self.patient.full_name
        context["patient"] = self.patient
        
        # Add prescription statistics (cached for performance)
        from django.core.cache import cache
        cache_key = f'prescription_stats_{self.patient.id}'
        stats = cache.get(cache_key)
        
        if stats is None:
            prescriptions = context['prescription_history']
            if hasattr(prescriptions, 'count'):
                total_prescriptions = prescriptions.count()
            else:
                total_prescriptions = len(prescriptions)
                
            # Get unique medicines prescribed
            unique_medicines = set()
            for prescription in context['prescription_history']:
                unique_medicines.add(prescription.medicine)
            
            stats = {
                'total_prescriptions': total_prescriptions,
                'unique_medicines': len(unique_medicines),
                'total_consultations': models.Consultation.objects.filter(
                    patient=self.patient
                ).count()
            }
            cache.set(cache_key, stats, 600)  # Cache for 10 minutes
        
        context['stats'] = stats
        return context
