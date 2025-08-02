from django.db import models
from django.db.models import Prefetch
from django.utils import timezone
from datetime import timedelta


class AppointmentManager(models.Manager):
    def with_related(self):
        """Optimize appointment queries with related data"""
        return self.select_related(
            'patient', 'doctor', 'updated_by'
        )
    
    def upcoming_appointments(self, days=7):
        """Get upcoming appointments within specified days"""
        end_date = timezone.now().date() + timedelta(days=days)
        return self.with_related().filter(
            appointment_date__gte=timezone.now().date(),
            appointment_date__lte=end_date
        ).order_by('appointment_date')
    
    def today_appointments(self):
        """Get today's appointments"""
        return self.with_related().filter(
            appointment_date=timezone.now().date()
        ).order_by('appointment_date')


class ConsultationManager(AppointmentManager):
    def with_full_details(self):
        """Get consultations with all related data including prescriptions"""
        return self.select_related(
            'patient', 'doctor', 'updated_by'
        ).prefetch_related(
            Prefetch(
                'consultation_prescription',
                to_attr='prescriptions'
            )
        )
    
    def recent_consultations(self, days=30):
        """Get recent consultations within specified days"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_full_details().filter(
            consultation_date__gte=start_date
        ).order_by('-consultation_date')
    
    def by_patient(self, patient):
        """Get all consultations for a specific patient"""
        return self.with_full_details().filter(
            patient=patient
        ).order_by('-consultation_date')
    
    def by_doctor(self, doctor):
        """Get all consultations for a specific doctor"""
        return self.with_full_details().filter(
            doctor=doctor
        ).order_by('-consultation_date')


class PrescriptionManager(models.Manager):
    def with_consultation_details(self):
        """Get prescriptions with consultation and patient details"""
        return self.select_related(
            'consultation__patient',
            'consultation__doctor',
            'updated_by'
        )
    
    def for_patient(self, patient):
        """Get all prescriptions for a specific patient"""
        return self.with_consultation_details().filter(
            consultation__patient=patient
        ).order_by('-consultation__consultation_date')
    
    def recent_prescriptions(self, days=30):
        """Get recent prescriptions within specified days"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_consultation_details().filter(
            consultation__consultation_date__gte=start_date
        ).order_by('-consultation__consultation_date')
