from django.db import models
from django.db.models import Prefetch


class PatientManager(models.Manager):
    def with_related(self):
        """Optimize patient queries with related data"""
        return self.select_related('updated_by')
    
    def with_consultations(self):
        """Get patients with their consultation data optimized"""
        from ayuh_consultation.models import Consultation
        
        return self.select_related('updated_by').prefetch_related(
            Prefetch(
                'consulting_patient',
                queryset=Consultation.objects.select_related(
                    'doctor', 'patient', 'updated_by'
                ).order_by('-consultation_date')
            )
        )
    
    def with_latest_consultation(self):
        """Get patients with only their latest consultation"""
        from ayuh_consultation.models import Consultation
        
        return self.select_related('updated_by').prefetch_related(
            Prefetch(
                'consulting_patient',
                queryset=Consultation.objects.select_related(
                    'doctor', 'updated_by'
                ).order_by('-consultation_date')[:1],
                to_attr='latest_consultation'
            )
        )
    
    def active_patients(self):
        """Get patients who have had consultations"""
        return self.with_consultations().filter(
            consulting_patient__isnull=False
        ).distinct()


class PatientProfileManager(PatientManager):
    def with_full_profile(self):
        """Get patient profiles with all related data"""
        return self.with_related()
