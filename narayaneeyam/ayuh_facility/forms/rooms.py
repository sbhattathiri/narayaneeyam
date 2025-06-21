from ayuh_facility.models.rooms import (
    Room,
)
from django import (
    forms,
)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_name",
            "room_type",
            "room_category",
            "room_location",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
