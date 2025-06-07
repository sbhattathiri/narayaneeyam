from ayuh_admission.models.admissions import Admission
from ayuh_core.models import AyuhModel
from django.db import (
    models,
)


class Canteen(AyuhModel):
    admission = models.ForeignKey(
        Admission,
        on_delete=models.SET_NULL,
        related_name="room_occupancy_admission",
    )
    order_date = models.DateField()
    meal_type = models.CharField(
        max_length=10,
        choices=[
            ("BREAKFAST", "Breakfast"),
            ("LUNCH", "Lunch"),
            ("DINNER", "Dinner"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_time"]
