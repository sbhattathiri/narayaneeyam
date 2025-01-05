from django.db import (
    models,
)
from django_pg_jsonschema.fields import (
    JSONSchemaField,
)

from ayuh_core.models import (
    AyuhModel,
)


class PatientAddress(AyuhModel):
    patient = models.OneToOneField(
        "Patient",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    billing_address = JSONSchemaField(
        schema={
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "address_line_1": {"type": "string"},
                "address_line_2": {"type": "string"},
                "address_line_3": {"type": "string"},
                "address_line_4": {"type": "string"},
                "PIN": {"type": "integer"},
            },
            "required": ["PIN"],
        },
        null=True,
        blank=True,
    )
    billing_address_is_shipping_address = models.BooleanField(default=False)
    shipping_address = JSONSchemaField(
        schema={
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "address_line_1": {"type": "string"},
                "address_line_2": {"type": "string"},
                "address_line_3": {"type": "string"},
                "address_line_4": {"type": "string"},
                "PIN": {"type": "integer"},
            },
            "required": ["PIN"],
        },
        null=True,
        blank=True,
    )
