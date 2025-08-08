import logging
from django.views.generic import ListView
from django.db.models import Prefetch
from django.core.paginator import Paginator

from ayuh_consultation import models

logger = logging.getLogger(__name__)


class OptimizedConsultationListView(ListView):
    model = models.Consultation
    template_name = "ayuh_consultation/list_consultation_template.html"
    context_object_name = "consultations"
    paginate_by = 25  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for patient, doctor, and updated_by
        2. Prefetching prescriptions if needed
        3. Adding proper ordering
        """
        return models.Consultation.objects.select_related(
            'patient',      # Avoid N+1 for patient data
            'doctor',       # Avoid N+1 for doctor data  
            'updated_by'    # Avoid N+1 for updated_by from AyuhModel
        ).prefetch_related(
            # Only prefetch prescriptions if you're using them in the template
            Prefetch(
                'consultation_prescription',
                to_attr='prescriptions'
            )
        ).order_by('-consultation_date')  # Most recent first

    def get_context_data(self, **kwargs):
        """Add additional context with optimized queries"""
        context = super().get_context_data(**kwargs)
        
        # Add summary statistics (cached for performance)
        from django.core.cache import cache
        from django.utils import timezone
        
        stats_key = 'consultation_list_stats'
        stats = cache.get(stats_key)
        
        if stats is None:
            today = timezone.now().date()
            stats = {
                'total_consultations': models.Consultation.objects.count(),
                'today_consultations': models.Consultation.objects.filter(
                    consultation_date__date=today
                ).count(),
                'this_month_consultations': models.Consultation.objects.filter(
                    consultation_date__month=today.month,
                    consultation_date__year=today.year
                ).count(),
            }
            cache.set(stats_key, stats, 300)  # Cache for 5 minutes
        
        context['stats'] = stats
        return context


class ConsultationsByPatientView(ListView):
    """Optimized view to show consultations for a specific patient"""
    model = models.Consultation
    template_name = "ayuh_consultation/patient_consultations.html"
    context_object_name = "consultations"
    paginate_by = 10

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return models.Consultation.objects.by_patient(
            patient_id
        ).select_related(
            'patient', 'doctor', 'updated_by'
        ).prefetch_related(
            'consultation_prescription'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs.get('patient_id')
        
        # Get patient info (cached)
        from ayuh_patient.models import Patient
        context['patient'] = Patient.objects.select_related('updated_by').get(
            id=patient_id
        )
        return context


class ConsultationsByDoctorView(ListView):
    """Optimized view to show consultations for a specific doctor"""
    model = models.Consultation
    template_name = "ayuh_consultation/doctor_consultations.html"
    context_object_name = "consultations"
    paginate_by = 25

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        return models.Consultation.objects.by_doctor(
            doctor_id
        ).select_related(
            'patient', 'doctor', 'updated_by'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor_id = self.kwargs.get('doctor_id')
        
        # Get doctor info
        from ayuh_staff.models import Staff
        context['doctor'] = Staff.objects.select_related('updated_by').get(
            id=doctor_id
        )
        return context


class TodayConsultationsView(ListView):
    """Optimized view for today's consultations"""
    model = models.Consultation
    template_name = "ayuh_consultation/today_consultations.html"
    context_object_name = "consultations"

    def get_queryset(self):
        from django.utils import timezone
        today = timezone.now().date()
        
        return models.Consultation.objects.select_related(
            'patient', 'doctor', 'updated_by'
        ).filter(
            consultation_date__date=today
        ).order_by('consultation_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.utils import timezone
        context['today'] = timezone.now().date()
        return context
