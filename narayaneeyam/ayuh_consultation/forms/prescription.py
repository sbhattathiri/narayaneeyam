from ayuh_consultation import (
    models,
)

from django.forms import (
    inlineformset_factory,
)

PrescriptionFormSet = inlineformset_factory(
    models.Consultation,
    models.Prescription,
    fields=("medicine", "instructions"),
    extra=3,
    can_delete=True,
)
