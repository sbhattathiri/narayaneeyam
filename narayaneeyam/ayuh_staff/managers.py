from django.db import models
from django.db.models import Prefetch
from django.utils import timezone


class StaffManager(models.Manager):
    def with_related(self):
        """Optimize staff queries with related data"""
        return self.select_related('updated_by')
    
    def active_staff(self):
        """Get active staff members"""
        return self.with_related().filter(active=True)
    
    def doctors(self):
        """Get all doctors"""
        from ayuh_core.enums import StaffRole
        return self.with_related().filter(
            designation=StaffRole.DOCTOR.value,
            active=True
        )
    
    def therapists(self):
        """Get all therapists"""
        from ayuh_core.enums import StaffRole
        return self.with_related().filter(
            designation=StaffRole.THERAPIST.value,
            active=True
        )
    
    def with_consultations(self):
        """Get staff with their consultation data"""
        return self.with_related().prefetch_related(
            Prefetch(
                'consulting_doctor',
                to_attr='consultations'
            )
        )
    
    def by_designation(self, designation):
        """Get staff by designation"""
        return self.with_related().filter(
            designation=designation,
            active=True
        )
