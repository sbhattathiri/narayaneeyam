import logging

from ayuh_inventory.forms import (
    MedicinesForm,
)
from ayuh_inventory.models import (
    Medicine,
)
from django.views.generic import (
    ListView,
)

logger = logging.getLogger(__name__)


class MedicineListView(ListView):
    model = Medicine
    template_name = "ayuh_inventory/list_medicine_template.html"
    context_object_name = "medicines"
    paginate_by = 25  # Add pagination for better performance

    def get_queryset(self):
        """
        OPTIMIZED VERSION - Eliminates N+1 queries by:
        1. Using select_related for manufacturer and updated_by
        2. Using prefetch_related for stock data with select_related
        3. Adding proper ordering
        """
        return Medicine.objects.select_related(
            'manufacturer',  # Avoid N+1 for manufacturer data
            'updated_by'     # Avoid N+1 for updated_by from AyuhModel
        ).prefetch_related(
            # Optimize stock prefetch with select_related
            'stock__updated_by'
        ).order_by('name')

    def get_context_data(self, **kwargs):
        """Add cached statistics for better performance"""
        context = super().get_context_data(**kwargs)
        
        # Add inventory statistics (cached for performance)
        from django.core.cache import cache
        from django.db.models import Sum, F
        
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
