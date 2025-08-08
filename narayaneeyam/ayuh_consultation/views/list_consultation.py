from django.views.generic import (
    ListView,
)

from ayuh_consultation import (
    models,
)


class ConsultationListView(ListView):
    model = models.Consultation
    template_name = "ayuh_consultation/list_consultation_template.html"
    context_object_name = "consultations"
    paginate_by = 25  # Add pagination for better performance

    def get_queryset(self):
        """
        OPTIMIZED VERSION - Eliminates N+1 queries by:
        1. Using select_related for patient, doctor, and updated_by
        2. Adding proper ordering
        3. Prefetching prescriptions if needed
        """
        return models.Consultation.objects.select_related(
            'patient',      # Avoid N+1 for patient data
            'doctor',       # Avoid N+1 for doctor data  
            'updated_by'    # Avoid N+1 for updated_by from AyuhModel
        ).order_by('-consultation_date')  # Most recent first

    def get_context_data(self, **kwargs):
        """Add cached statistics for better performance"""
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
