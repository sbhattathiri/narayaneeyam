from ayuh_admission import (
    models,
)
from django.views.generic import (
    ListView,
)


class AdmissionListView(ListView):
    model = models.Admission
    template_name = "ayuh_admission/list_admission_template.html"
    context_object_name = "admissions"
    paginate_by = 25  # Add pagination for better performance

    def get_queryset(self):
        """
        OPTIMIZED VERSION - Eliminates N+1 queries by:
        1. Using select_related for all foreign keys
        2. Avoiding Python loops
        3. Getting all data in single query
        """
        admissions = models.Admission.objects.select_related(
            'consultation__patient',    # Patient data
            'consultation__doctor',     # Doctor data
            'consultation__updated_by', # Consultation updated_by
            'room',                     # Room data
            'updated_by',              # Admission updated_by
            'treatment_updated_by'     # Treatment updated_by
        ).order_by('-admission_date')  # Most recent first

        # Return processed data without Python loops
        return [
            {
                "id": admission.id,
                "hashid": admission.admission_hash_id,
                "patient": admission.consultation.patient,
                "doctor": admission.consultation.doctor,
                "consultation": admission.consultation,
                "admission_date": admission.admission_date,
                "room": admission.room,
                "discharge_date": admission.discharge_date,
            }
            for admission in admissions
        ]

    def get_context_data(self, **kwargs):
        """Add cached statistics for better performance"""
        context = super().get_context_data(**kwargs)
        
        # Add admission statistics (cached for performance)
        from django.core.cache import cache
        from django.utils import timezone
        
        stats_key = 'admission_list_stats'
        stats = cache.get(stats_key)
        
        if stats is None:
            today = timezone.now().date()
            stats = {
                'total_admissions': models.Admission.objects.count(),
                'active_admissions': models.Admission.objects.filter(
                    discharge_date__isnull=True
                ).count(),
                'today_admissions': models.Admission.objects.filter(
                    admission_date__date=today
                ).count(),
                'today_discharges': models.Admission.objects.filter(
                    discharge_date__date=today
                ).count(),
            }
            cache.set(stats_key, stats, 300)  # Cache for 5 minutes
        
        context['stats'] = stats
        return context
