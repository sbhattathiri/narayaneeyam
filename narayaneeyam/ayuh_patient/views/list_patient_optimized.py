import logging
from django.db.models import (
    F,
    OuterRef,
    Subquery,
    Value,
    Prefetch,
)
from django.db.models.functions import (
    Coalesce,
    Concat,
)
from django.views.generic import (
    ListView,
)
from django.core.paginator import Paginator

from ayuh_consultation.models import (
    Appointment,
)
from ayuh_patient.models import (
    PatientProfile,
)

logger = logging.getLogger(__name__)


class OptimizedPatientListView(ListView):
    model = PatientProfile
    template_name = "ayuh_patient/list_patient_template.html"
    context_object_name = "patients"
    slug_field = "patient_hash_id"
    paginate_by = 25  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for foreign keys
        2. Using subqueries for latest appointment data
        3. Avoiding loops in Python code
        """
        # Subquery to get latest appointment data
        latest_appointments = Appointment.objects.filter(
            patient=OuterRef("pk")
        ).select_related('doctor').order_by("-appointment_date")

        # Annotate patients with latest appointment data
        patients = PatientProfile.objects.select_related(
            'updated_by'  # Optimize the foreign key from AyuhModel
        ).annotate(
            # Get latest doctor's full name
            latest_appointment_doctor_full_name=Subquery(
                latest_appointments.annotate(
                    doctor_full_name=Concat(
                        Coalesce(F("doctor__title"), Value("")),
                        Value(" "),
                        Coalesce(F("doctor__first_name"), Value("")),
                        Value(" "),
                        Coalesce(F("doctor__middle_name"), Value("")),
                        Value(" "),
                        Coalesce(F("doctor__last_name"), Value("")),
                    )
                ).values("doctor_full_name")[:1]
            ),
            # Get latest appointment date
            latest_appointment_date=Subquery(
                latest_appointments.values("appointment_date")[:1]
            ),
        ).order_by('-created_at')  # Add consistent ordering

        return patients

    def get_context_data(self, **kwargs):
        """Add additional context if needed"""
        context = super().get_context_data(**kwargs)
        
        # Add summary statistics (cached for performance)
        from django.core.cache import cache
        stats_key = 'patient_list_stats'
        stats = cache.get(stats_key)
        
        if stats is None:
            stats = {
                'total_patients': PatientProfile.objects.count(),
                'patients_with_appointments': PatientProfile.objects.filter(
                    consulting_patient__isnull=False
                ).distinct().count(),
            }
            cache.set(stats_key, stats, 300)  # Cache for 5 minutes
        
        context['stats'] = stats
        return context


# Alternative implementation using prefetch_related for better performance
# when you need to access multiple appointments per patient
class PatientListWithMultipleAppointmentsView(ListView):
    model = PatientProfile
    template_name = "ayuh_patient/list_patient_template.html"
    context_object_name = "patients"
    paginate_by = 25

    def get_queryset(self):
        """
        Use this when you need to access multiple appointments per patient
        """
        return PatientProfile.objects.select_related(
            'updated_by'
        ).prefetch_related(
            Prefetch(
                'consulting_patient',
                queryset=Appointment.objects.select_related(
                    'doctor', 'updated_by'
                ).order_by('-appointment_date'),
                to_attr='appointments'
            )
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Process patients to add latest appointment data
        processed_patients = []
        for patient in context['patients']:
            appointments = getattr(patient, 'appointments', [])
            latest_appointment = appointments[0] if appointments else None
            
            processed_patients.append({
                'patient_hash_id': patient.patient_hash_id,
                'patient': patient,
                'doctor': latest_appointment.doctor if latest_appointment else None,
                'appointment_date': latest_appointment.appointment_date if latest_appointment else None,
            })
        
        context['patients'] = processed_patients
        return context
