import logging
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator

from ayuh_consultation import models
from ayuh_patient.models import Patient

logger = logging.getLogger(__name__)


class OptimizedPrescriptionHistoryListView(ListView):
    model = models.Prescription
    template_name = "ayuh_consultation/list_prescription_history_template.html"
    context_object_name = "prescription_history"
    paginate_by = 20  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for consultation, patient, and doctor
        2. Getting patient once and reusing
        3. Proper ordering
        """
        # Get patient once with optimized query
        self.patient = get_object_or_404(
            Patient.objects.select_related('updated_by'),
            patient_registration_id=self.kwargs["patient_registration_id"]
        )

        # Get prescriptions with all related data in one query
        return models.Prescription.objects.select_related(
            'consultation__patient',    # Patient data
            'consultation__doctor',     # Doctor data
            'consultation__updated_by', # Consultation updated_by
            'updated_by'               # Prescription updated_by
        ).filter(
            consultation__patient=self.patient
        ).order_by('-consultation__consultation_date')  # Most recent first

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_registration_id"] = self.patient.patient_registration_id
        context["patient_full_name"] = self.patient.full_name
        context["patient"] = self.patient
        
        # Add prescription statistics
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


class PrescriptionsByMedicineView(ListView):
    """View to show all prescriptions for a specific medicine"""
    model = models.Prescription
    template_name = "ayuh_consultation/prescriptions_by_medicine.html"
    context_object_name = "prescriptions"
    paginate_by = 25

    def get_queryset(self):
        medicine_name = self.kwargs.get('medicine_name')
        return models.Prescription.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'updated_by'
        ).filter(
            medicine__icontains=medicine_name
        ).order_by('-consultation__consultation_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine_name'] = self.kwargs.get('medicine_name')
        return context


class RecentPrescriptionsView(ListView):
    """View to show recent prescriptions across all patients"""
    model = models.Prescription
    template_name = "ayuh_consultation/recent_prescriptions.html"
    context_object_name = "prescriptions"
    paginate_by = 50

    def get_queryset(self):
        return models.Prescription.objects.recent_prescriptions(
            days=30
        ).select_related(
            'consultation__patient',
            'consultation__doctor',
            'updated_by'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add medicine frequency analysis
        from django.db.models import Count
        from django.core.cache import cache
        
        cache_key = 'recent_medicine_frequency'
        medicine_frequency = cache.get(cache_key)
        
        if medicine_frequency is None:
            medicine_frequency = models.Prescription.objects.recent_prescriptions(
                days=30
            ).values('medicine').annotate(
                count=Count('medicine')
            ).order_by('-count')[:10]
            cache.set(cache_key, medicine_frequency, 1800)  # Cache for 30 minutes
        
        context['medicine_frequency'] = medicine_frequency
        return context
