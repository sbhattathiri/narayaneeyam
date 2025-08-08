import logging
from django.views.generic import ListView
from django.db.models import Prefetch, Sum, F
from django.core.paginator import Paginator

from ayuh_inventory.models import Medicine, MedicineStock
from ayuh_inventory.forms import MedicinesForm

logger = logging.getLogger(__name__)


class OptimizedMedicineListView(ListView):
    model = Medicine
    template_name = "ayuh_inventory/list_medicine_template.html"
    context_object_name = "medicines"
    paginate_by = 25  # Add pagination

    def get_queryset(self):
        """
        Optimized queryset that eliminates N+1 queries by:
        1. Using select_related for manufacturer and updated_by
        2. Using prefetch_related for stock data
        3. Annotating with stock quantities
        """
        return Medicine.objects.select_related(
            'manufacturer',  # Avoid N+1 for manufacturer data
            'updated_by'     # Avoid N+1 for updated_by from AyuhModel
        ).prefetch_related(
            Prefetch(
                'stock',
                queryset=MedicineStock.objects.select_related('updated_by'),
                to_attr='stock_info'
            )
        ).annotate(
            # Calculate total stock quantity
            total_stock=Sum('stock__quantity')
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add inventory statistics (cached for performance)
        from django.core.cache import cache
        
        stats_key = 'medicine_inventory_stats'
        stats = cache.get(stats_key)
        
        if stats is None:
            stats = {
                'total_medicines': Medicine.objects.count(),
                'low_stock_count': Medicine.objects.filter(
                    stock__quantity__lte=10
                ).distinct().count(),
                'out_of_stock_count': Medicine.objects.filter(
                    stock__quantity=0
                ).distinct().count(),
                'total_stock_value': Medicine.objects.aggregate(
                    total_value=Sum(F('price') * F('stock__quantity'))
                )['total_value'] or 0
            }
            cache.set(stats_key, stats, 600)  # Cache for 10 minutes
        
        context['stats'] = stats
        return context


class LowStockMedicinesView(ListView):
    """View to show medicines with low stock"""
    model = Medicine
    template_name = "ayuh_inventory/low_stock_medicines.html"
    context_object_name = "medicines"
    paginate_by = 25

    def get_queryset(self):
        threshold = int(self.request.GET.get('threshold', 10))
        return Medicine.objects.select_related(
            'manufacturer', 'updated_by'
        ).prefetch_related(
            'stock'
        ).filter(
            stock__quantity__lte=threshold
        ).distinct().order_by('stock__quantity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['threshold'] = int(self.request.GET.get('threshold', 10))
        return context


class MedicinesByTypeView(ListView):
    """View to show medicines filtered by type"""
    model = Medicine
    template_name = "ayuh_inventory/medicines_by_type.html"
    context_object_name = "medicines"
    paginate_by = 25

    def get_queryset(self):
        medicine_type = self.kwargs.get('medicine_type')
        return Medicine.objects.select_related(
            'manufacturer', 'updated_by'
        ).prefetch_related(
            'stock'
        ).filter(
            type=medicine_type
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine_type'] = self.kwargs.get('medicine_type')
        
        # Get type statistics
        from django.db.models import Count, Avg
        type_stats = Medicine.objects.filter(
            type=context['medicine_type']
        ).aggregate(
            count=Count('id'),
            avg_price=Avg('price'),
            total_stock=Sum('stock__quantity')
        )
        context['type_stats'] = type_stats
        return context


class MedicineSearchView(ListView):
    """Optimized search view for medicines"""
    model = Medicine
    template_name = "ayuh_inventory/medicine_search.html"
    context_object_name = "medicines"
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if not query:
            return Medicine.objects.none()
        
        return Medicine.objects.select_related(
            'manufacturer', 'updated_by'
        ).prefetch_related(
            'stock'
        ).filter(
            name__icontains=query
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
