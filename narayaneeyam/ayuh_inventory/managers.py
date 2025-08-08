from django.db import models
from django.db.models import Prefetch, Sum, F
from django.utils import timezone
from datetime import timedelta


class MedicineManager(models.Manager):
    def with_related(self):
        """Optimize medicine queries with manufacturer and stock data"""
        return self.select_related('manufacturer', 'updated_by')
    
    def with_stock_info(self):
        """Get medicines with their current stock information"""
        return self.with_related().prefetch_related(
            Prefetch(
                'stock',
                to_attr='current_stock'
            )
        )
    
    def with_sales_data(self):
        """Get medicines with their sales data"""
        return self.with_related().prefetch_related(
            Prefetch(
                'medicinesaleitem_set',
                to_attr='sales_items'
            )
        )
    
    def low_stock(self, threshold=10):
        """Get medicines with low stock"""
        return self.with_stock_info().filter(
            stock__quantity__lte=threshold
        )
    
    def by_type(self, medicine_type):
        """Get medicines by type"""
        return self.with_related().filter(type=medicine_type)


class MedicineSaleManager(models.Manager):
    def with_full_details(self):
        """Get sales with all related data"""
        return self.select_related(
            'patient', 'updated_by'
        ).prefetch_related(
            Prefetch(
                'items',
                queryset=models.get_model('ayuh_inventory', 'MedicineSaleItem').objects.select_related(
                    'medicine__manufacturer'
                ),
                to_attr='sale_items'
            ),
            Prefetch(
                'payment',
                to_attr='payment_info'
            )
        )
    
    def recent_sales(self, days=30):
        """Get recent sales within specified days"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_full_details().filter(
            sale_date__gte=start_date
        ).order_by('-sale_date')
    
    def by_patient(self, patient):
        """Get all sales for a specific patient"""
        return self.with_full_details().filter(
            patient=patient
        ).order_by('-sale_date')
    
    def today_sales(self):
        """Get today's sales"""
        return self.with_full_details().filter(
            sale_date__date=timezone.now().date()
        ).order_by('-sale_date')


class MedicineSaleItemManager(models.Manager):
    def with_related(self):
        """Get sale items with medicine and sale details"""
        return self.select_related(
            'sale__patient',
            'medicine__manufacturer',
            'updated_by'
        )
    
    def by_medicine(self, medicine):
        """Get all sale items for a specific medicine"""
        return self.with_related().filter(
            medicine=medicine
        ).order_by('-sale__sale_date')
    
    def recent_items(self, days=30):
        """Get recent sale items"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_related().filter(
            sale__sale_date__gte=start_date
        ).order_by('-sale__sale_date')


class MedicineSalePaymentInfoManager(models.Manager):
    def with_sale_details(self):
        """Get payment info with sale details"""
        return self.select_related(
            'sale__patient',
            'updated_by'
        )
    
    def pending_payments(self):
        """Get payments with outstanding amounts"""
        return self.with_sale_details().filter(
            amount_due__gt=0
        ).order_by('payment_due_date')
    
    def overdue_payments(self):
        """Get overdue payments"""
        return self.with_sale_details().filter(
            amount_due__gt=0,
            payment_due_date__lt=timezone.now()
        ).order_by('payment_due_date')


class MedicineStockManager(models.Manager):
    def with_medicine_details(self):
        """Get stock with medicine details"""
        return self.select_related(
            'medicine__manufacturer',
            'updated_by'
        )
    
    def low_stock_items(self, threshold=10):
        """Get items with low stock"""
        return self.with_medicine_details().filter(
            quantity__lte=threshold
        )
    
    def out_of_stock(self):
        """Get out of stock items"""
        return self.with_medicine_details().filter(quantity=0)


class MedicinePurchaseManager(models.Manager):
    def with_related(self):
        """Get purchases with medicine details"""
        return self.select_related(
            'medicine__manufacturer',
            'updated_by'
        )
    
    def recent_purchases(self, days=30):
        """Get recent purchases"""
        start_date = timezone.now() - timedelta(days=days)
        return self.with_related().filter(
            purchase_date__gte=start_date
        ).order_by('-purchase_date')
