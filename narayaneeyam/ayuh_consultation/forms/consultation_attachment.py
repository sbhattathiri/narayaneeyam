from django.forms import (
    inlineformset_factory,
)

from ayuh_consultation import (
    models,
)

ConsultationAttachmentFormSet = inlineformset_factory(
    models.Consultation,
    models.ConsultationAttachment,
    fields=("attachment",),
    extra=2,
    can_delete=True,
)
