from django.forms import (
    inlineformset_factory,
)

from ayuh_consultation import (
    models,
)

PrescriptionFormSet = inlineformset_factory(
    models.Consultation,
    models.Prescription,
    fields=("medicine", "instructions"),
    extra=2,
    can_delete=True,
)
