from django.db import models
from django.db.models import Prefetch
from django.utils import timezone


class RoomManager(models.Manager):
    def with_related(self):
        """Optimize room queries with related data"""
        return self.select_related('updated_by')
    
    def with_occupancy(self):
        """Get rooms with their occupancy data"""
        return self.with_related().prefetch_related(
            Prefetch(
                'admission_set',
                queryset=models.get_model('ayuh_admission', 'Admission').objects.select_related(
                    'consultation__patient',
                    'consultation__doctor'
                ).filter(discharge_date__isnull=True),
                to_attr='current_occupancy'
            )
        )
    
    def available_rooms(self):
        """Get available rooms (not currently occupied)"""
        from ayuh_admission.models import Admission
        occupied_room_ids = Admission.objects.filter(
            discharge_date__isnull=True
        ).values_list('room_id', flat=True)
        
        return self.with_related().exclude(
            id__in=occupied_room_ids
        )
    
    def occupied_rooms(self):
        """Get currently occupied rooms"""
        from ayuh_admission.models import Admission
        occupied_room_ids = Admission.objects.filter(
            discharge_date__isnull=True
        ).values_list('room_id', flat=True)
        
        return self.with_occupancy().filter(
            id__in=occupied_room_ids
        )
    
    def by_category(self, category):
        """Get rooms by category"""
        return self.with_related().filter(room_category=category)
    
    def by_type(self, room_type):
        """Get rooms by type"""
        return self.with_related().filter(room_type=room_type)


class RoomOccupancyManager(models.Manager):
    def with_related(self):
        """Get occupancy with room and patient details"""
        return self.select_related(
            'room',
            'patient',
            'updated_by'
        )
    
    def current_occupancy(self):
        """Get current room occupancy"""
        return self.with_related().filter(
            check_out_date__isnull=True
        )
    
    def by_room(self, room):
        """Get occupancy history for a specific room"""
        return self.with_related().filter(
            room=room
        ).order_by('-check_in_date')
    
    def by_patient(self, patient):
        """Get occupancy history for a specific patient"""
        return self.with_related().filter(
            patient=patient
        ).order_by('-check_in_date')
