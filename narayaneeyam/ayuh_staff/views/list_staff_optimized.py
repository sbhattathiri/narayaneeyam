import logging
from django.views.generic import ListView
from django.db.models import Count, Prefetch
from django.core.paginator import Paginator

from ayuh_staff import models

logger = logging.getLogger(__name__)


class OptimizedStaffListView(ListView):
    model = models.Staff
    template_name = "ayuh_staff/list_staff_template.html"
    context_object_name = "staffs"
    slug_field = "staff_hash_id"
    paginate_by = 25  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for updated_by
        2. Prefetching consultation data if needed
        3. Filtering active staff
        """
        return models.Staff.objects.select_related(
            'updated_by'  # Avoid N+1 for updated_by from AyuhModel
        ).filter(
            active=True  # Only show active staff
        ).prefetch_related(
            # Only prefetch if you're showing consultation counts
            Prefetch(
                'consulting_doctor',
                to_attr='consultations'
            )
        ).order_by('designation', 'last_name', 'first_name')

    def get_context_data(self, **kwargs):
        """Add additional context with optimized queries"""
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


class DoctorsListView(ListView):
    """Optimized view to show only doctors"""
    model = models.Staff
    template_name = "ayuh_staff/doctors_list.html"
    context_object_name = "doctors"
    paginate_by = 25

    def get_queryset(self):
        from ayuh_core.enums import StaffRole
        return models.Staff.objects.select_related(
            'updated_by'
        ).filter(
            designation=StaffRole.DOCTOR.value,
            active=True
        ).prefetch_related(
            # Get consultation statistics
            Prefetch(
                'consulting_doctor',
                to_attr='consultations'
            )
        ).order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add doctor-specific statistics
        from django.utils import timezone
        from django.db.models import Count
        from ayuh_consultation.models import Consultation
        
        # Get consultation counts for each doctor (optimized)
        doctor_stats = Consultation.objects.filter(
            doctor__in=context['doctors']
        ).values('doctor').annotate(
            consultation_count=Count('id')
        )
        
        # Create a lookup dictionary
        stats_dict = {stat['doctor']: stat['consultation_count'] for stat in doctor_stats}
        
        # Add stats to each doctor
        for doctor in context['doctors']:
            doctor.consultation_count = stats_dict.get(doctor.id, 0)
        
        return context


class TherapistsListView(ListView):
    """Optimized view to show only therapists"""
    model = models.Staff
    template_name = "ayuh_staff/therapists_list.html"
    context_object_name = "therapists"
    paginate_by = 25

    def get_queryset(self):
        from ayuh_core.enums import StaffRole
        return models.Staff.objects.select_related(
            'updated_by'
        ).filter(
            designation=StaffRole.THERAPIST.value,
            active=True
        ).order_by('last_name', 'first_name')


class StaffByDesignationView(ListView):
    """Generic view to show staff by designation"""
    model = models.Staff
    template_name = "ayuh_staff/staff_by_designation.html"
    context_object_name = "staff_members"
    paginate_by = 25

    def get_queryset(self):
        designation = self.kwargs.get('designation')
        return models.Staff.objects.select_related(
            'updated_by'
        ).filter(
            designation=designation,
            active=True
        ).order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['designation'] = self.kwargs.get('designation')
        
        # Get designation-specific statistics
        designation = context['designation']
        staff_count = models.Staff.objects.filter(
            designation=designation,
            active=True
        ).count()
        
        context['designation_stats'] = {
            'total_count': staff_count,
            'designation_name': designation
        }
        return context


class InactiveStaffView(ListView):
    """View to show inactive staff members"""
    model = models.Staff
    template_name = "ayuh_staff/inactive_staff.html"
    context_object_name = "inactive_staff"
    paginate_by = 25

    def get_queryset(self):
        return models.Staff.objects.select_related(
            'updated_by'
        ).filter(
            active=False
        ).order_by('-date_of_leaving', 'last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add inactive staff statistics
        from django.db.models import Count
        from django.utils import timezone
        from datetime import timedelta
        
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        
        stats = {
            'total_inactive': models.Staff.objects.filter(active=False).count(),
            'recently_left': models.Staff.objects.filter(
                active=False,
                date_of_leaving__gte=thirty_days_ago
            ).count(),
        }
        
        context['inactive_stats'] = stats
        return context


class StaffSearchView(ListView):
    """Optimized search view for staff"""
    model = models.Staff
    template_name = "ayuh_staff/staff_search.html"
    context_object_name = "staff_members"
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            return models.Staff.objects.none()
        
        return models.Staff.objects.select_related(
            'updated_by'
        ).filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(email__icontains=query),
            active=True
        ).order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
