from ayuh_facility.models.room_occupancy import (
    RoomOccupancy,
)
from django import (
    forms,
)


class RoomOccupancyForm(forms.ModelForm):
    class Meta:
        model = RoomOccupancy
        fields = [
            "admission",
            "room",
            "start_date",
            "end_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
