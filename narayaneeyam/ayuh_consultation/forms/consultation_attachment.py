from ayuh_consultation import (
    models,
)

from django.forms import (
    inlineformset_factory,
)

ConsultationAttachmentFormSet = inlineformset_factory(
    models.Consultation,
    models.ConsultationAttachment,
    fields=("attachment",),
    extra=2,
    can_delete=True,
)
