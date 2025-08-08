import logging

from django.views.generic import (
    ListView,
)

from ayuh_staff import (
    models,
)

logger = logging.getLogger(__name__)


class StaffListView(ListView):
    model = models.Staff
    template_name = "ayuh_staff/list_staff_template.html"
    context_object_name = "staffs"
    slug_field = "staff_hash_id"
    paginate_by = 25  # Add pagination for better performance

    def get_queryset(self):
        """
        OPTIMIZED VERSION - Eliminates N+1 queries by:
        1. Using select_related for updated_by
        2. Filtering active staff
        3. Adding proper ordering
        """
        return models.Staff.objects.select_related(
            'updated_by'  # Avoid N+1 for updated_by from AyuhModel
        ).filter(
            active=True  # Only show active staff
        ).order_by('designation', 'last_name', 'first_name')

    def get_context_data(self, **kwargs):
        """Add cached statistics for better performance"""
        context = super().get_context_data(**kwargs)
        
        # Add staff statistics (cached for performance)
        from django.core.cache import cache
        from ayuh_core.enums import StaffRole
        
        stats_key = 'staff_list_stats'
        stats = cache.get(stats_key)
        
        if stats is None:
            stats = {
                'total_staff': models.Staff.objects.filter(active=True).count(),
                'doctors_count': models.Staff.objects.filter(
                    designation=StaffRole.DOCTOR.value,
                    active=True
                ).count(),
                'therapists_count': models.Staff.objects.filter(
                    designation=StaffRole.THERAPIST.value,
                    active=True
                ).count(),
                'total_inactive': models.Staff.objects.filter(active=False).count(),
            }
            cache.set(stats_key, stats, 600)  # Cache for 10 minutes
        
        context['stats'] = stats
        return context
