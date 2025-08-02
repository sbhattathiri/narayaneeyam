from django.db import models
from django.db.models import Prefetch
from django.utils import timezone
from datetime import timedelta


class AdmissionManager(models.Manager):
    def with_full_details(self):
        """Get admissions with all related data"""
        return self.select_related(
            'consultation__patient',
            'consultation__doctor', 
            'room',
            'updated_by',
            'treatment_updated_by'
        ).prefetch_related(
            Prefetch(
                'admission_treatments',
                to_attr='treatments'
            )
        )
    
    def active_admissions(self):
        """Get currently active admissions (not discharged)"""
        return self.with_full_details().filter(
            discharge_date__isnull=True
        ).order_by('-admission_date')
    
    def recent_admissions(self, days=30):
        """Get recent admissions within specified days"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_full_details().filter(
            admission_date__gte=start_date
        ).order_by('-admission_date')
    
    def by_patient(self, patient):
        """Get all admissions for a specific patient"""
        return self.with_full_details().filter(
            consultation__patient=patient
        ).order_by('-admission_date')
    
    def by_doctor(self, doctor):
        """Get all admissions for a specific doctor"""
        return self.with_full_details().filter(
            consultation__doctor=doctor
        ).order_by('-admission_date')
    
    def by_room(self, room):
        """Get all admissions for a specific room"""
        return self.with_full_details().filter(
            room=room
        ).order_by('-admission_date')
    
    def discharged_admissions(self):
        """Get discharged admissions"""
        return self.with_full_details().filter(
            discharge_date__isnull=False
        ).order_by('-discharge_date')
    
    def today_admissions(self):
        """Get today's admissions"""
        return self.with_full_details().filter(
            admission_date__date=timezone.now().date()
        ).order_by('-admission_date')
    
    def today_discharges(self):
        """Get today's discharges"""
        return self.with_full_details().filter(
            discharge_date__date=timezone.now().date()
        ).order_by('-discharge_date')


class AdmissionTreatmentManager(models.Manager):
    def with_admission_details(self):
        """Get treatments with admission details"""
        return self.select_related(
            'admission__consultation__patient',
            'admission__consultation__doctor',
            'admission__room',
            'updated_by'
        )
    
    def for_admission(self, admission):
        """Get all treatments for a specific admission"""
        return self.with_admission_details().filter(
            admission=admission
        ).order_by('-created_at')
    
    def recent_treatments(self, days=7):
        """Get recent treatments"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_admission_details().filter(
            created_at__gte=start_date
        ).order_by('-created_at')
