import logging
from django.views.generic import ListView
from django.db.models import Prefetch
from django.core.paginator import Paginator

from ayuh_admission import models

logger = logging.getLogger(__name__)


class OptimizedAdmissionListView(ListView):
    model = models.Admission
    template_name = "ayuh_admission/list_admission_template.html"
    context_object_name = "admissions"
    paginate_by = 25  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for all foreign keys
        2. Avoiding Python loops
        3. Getting all data in single query
        """
        return models.Admission.objects.select_related(
            'consultation__patient',    # Patient data
            'consultation__doctor',     # Doctor data
            'consultation__updated_by', # Consultation updated_by
            'room',                     # Room data
            'updated_by',              # Admission updated_by
            'treatment_updated_by'     # Treatment updated_by
        ).prefetch_related(
            # Prefetch treatments if needed
            Prefetch(
                'admission_treatments',
                to_attr='treatments'
            )
        ).order_by('-admission_date')  # Most recent first

    def get_context_data(self, **kwargs):
        """Add additional context with optimized queries"""
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


class ActiveAdmissionsView(ListView):
    """View to show only active (not discharged) admissions"""
    model = models.Admission
    template_name = "ayuh_admission/active_admissions.html"
    context_object_name = "admissions"
    paginate_by = 25

    def get_queryset(self):
        return models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room',
            'updated_by'
        ).filter(
            discharge_date__isnull=True
        ).order_by('-admission_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add room occupancy statistics
        from ayuh_facility.models import Room
        from django.core.cache import cache
        
        cache_key = 'room_occupancy_stats'
        room_stats = cache.get(cache_key)
        
        if room_stats is None:
            total_rooms = Room.objects.count()
            occupied_rooms = models.Admission.objects.filter(
                discharge_date__isnull=True
            ).values('room').distinct().count()
            
            room_stats = {
                'total_rooms': total_rooms,
                'occupied_rooms': occupied_rooms,
                'available_rooms': total_rooms - occupied_rooms,
                'occupancy_rate': (occupied_rooms / total_rooms * 100) if total_rooms > 0 else 0
            }
            cache.set(cache_key, room_stats, 600)  # Cache for 10 minutes
        
        context['room_stats'] = room_stats
        return context


class AdmissionsByPatientView(ListView):
    """View to show admission history for a specific patient"""
    model = models.Admission
    template_name = "ayuh_admission/patient_admissions.html"
    context_object_name = "admissions"
    paginate_by = 10

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room',
            'updated_by'
        ).filter(
            consultation__patient_id=patient_id
        ).order_by('-admission_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs.get('patient_id')
        
        # Get patient info
        from ayuh_patient.models import Patient
        context['patient'] = Patient.objects.select_related('updated_by').get(
            id=patient_id
        )
        
        # Add patient admission statistics
        admissions = context['admissions']
        if hasattr(admissions, 'count'):
            total_admissions = admissions.count()
        else:
            total_admissions = len(admissions)
        
        active_admissions = models.Admission.objects.filter(
            consultation__patient_id=patient_id,
            discharge_date__isnull=True
        ).count()
        
        context['patient_stats'] = {
            'total_admissions': total_admissions,
            'active_admissions': active_admissions,
        }
        return context


class AdmissionsByDoctorView(ListView):
    """View to show admissions for a specific doctor"""
    model = models.Admission
    template_name = "ayuh_admission/doctor_admissions.html"
    context_object_name = "admissions"
    paginate_by = 25

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        return models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room',
            'updated_by'
        ).filter(
            consultation__doctor_id=doctor_id
        ).order_by('-admission_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor_id = self.kwargs.get('doctor_id')
        
        # Get doctor info
        from ayuh_staff.models import Staff
        context['doctor'] = Staff.objects.select_related('updated_by').get(
            id=doctor_id
        )
        return context


class AdmissionsByRoomView(ListView):
    """View to show admission history for a specific room"""
    model = models.Admission
    template_name = "ayuh_admission/room_admissions.html"
    context_object_name = "admissions"
    paginate_by = 25

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room',
            'updated_by'
        ).filter(
            room_id=room_id
        ).order_by('-admission_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs.get('room_id')
        
        # Get room info
        from ayuh_facility.models import Room
        context['room'] = Room.objects.select_related('updated_by').get(
            id=room_id
        )
        
        # Check if room is currently occupied
        current_admission = models.Admission.objects.filter(
            room_id=room_id,
            discharge_date__isnull=True
        ).select_related('consultation__patient').first()
        
        context['current_admission'] = current_admission
        return context


class TodayAdmissionsView(ListView):
    """View for today's admissions and discharges"""
    model = models.Admission
    template_name = "ayuh_admission/today_admissions.html"
    context_object_name = "admissions"

    def get_queryset(self):
        from django.utils import timezone
        today = timezone.now().date()
        
        return models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room',
            'updated_by'
        ).filter(
            admission_date__date=today
        ).order_by('-admission_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.utils import timezone
        
        today = timezone.now().date()
        context['today'] = today
        
        # Get today's discharges
        today_discharges = models.Admission.objects.select_related(
            'consultation__patient',
            'consultation__doctor',
            'room'
        ).filter(
            discharge_date__date=today
        ).order_by('-discharge_date')
        
        context['today_discharges'] = today_discharges
        return context
