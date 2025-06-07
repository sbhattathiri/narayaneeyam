from ayuh_admission.models.admissions import Admission
from ayuh_core.enums import StaffRole
from ayuh_core.models import AyuhModel
from django.db import (
    models,
)

from ayuh_staff.models import Staff


class Treatment(AyuhModel):
    admission = models.ForeignKey(
        Admission,
        on_delete=models.SET_NULL,
        related_name="treatment_admission",
    )
    treatment = models.TextField(null=True, blank=True)
    therapist = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        limit_choices_to={"designation": StaffRole.THERAPIST.value},
        db_column="doctor",
        null=True,
        blank=True,
        related_name="treatment_therapist",
    )
    treatment_date = models.DateField()
    treatment_feedback = models.TextField(null=True, blank=True)
